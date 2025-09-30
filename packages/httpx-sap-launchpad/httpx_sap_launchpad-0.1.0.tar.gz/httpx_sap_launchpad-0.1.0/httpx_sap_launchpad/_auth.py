import asyncio
import json
import re
import threading
from collections.abc import AsyncGenerator, Generator
from typing import Any
from urllib.parse import parse_qs, quote_plus
from uuid import uuid4

import httpx
from httpx._config import DEFAULT_MAX_REDIRECTS

from ._constants import (
    HEADERS_COMMON,
    HEADERS_GIGYA,
    URL_ACCOUNT_CDC_API,
    URL_ACCOUNT_CORE_API,
    URL_ACCOUNT_SAML_PROXY,
    URL_ACCOUNT_SSO_IDP,
    URL_ACCOUNTS,
    URL_GIGYA_SDK,
    URL_LAUNCHPAD,
    URL_SUPPORT_PORTAL,
)
from ._exceptions import (
    SAPLaunchpadAuthBadGatewayError,
    SAPLaunchpadAuthForbiddenError,
    SAPLaunchpadAuthUnauthorizedError,
)
from ._html import endpoint_metadata_tuple_from_res
from ._httpx import build_redirect_request


class SAPLaunchpadAuth(httpx.Auth):
    def __init__(
        self,
        user_id: str,
        password: str,
    ) -> None:
        if not re.match(r"^[sS]\d+$", user_id):
            raise ValueError("Expected SAP Universal ID")

        # params
        self._user_id = user_id
        self._password = password

        # locks
        self._lock_async = asyncio.Lock()
        self._lock_sync = threading.RLock()

        # state, only altered within locks
        self._cookies = httpx.Cookies()
        self._login_id = uuid4()

    def sync_auth_flow(
        self,
        request: httpx.Request,
    ) -> Generator[httpx.Request, httpx.Response, None]:
        # ignore requests to specific resources
        accept = request.headers.get("Accept", "")
        is_specific = accept and accept not in ("*/*", "application/json")
        if is_specific:
            yield from self._send_through_client(request)
            return

        # inject headers and try request
        headers = httpx.Headers({"Accept": "application/json"})
        headers.update(request.headers)
        request.headers = headers
        res = yield from self._send_through_client(request)

        # if we're not logged out we were successful
        content_type = res.headers.get("Content-Type", "")
        is_logged_out = content_type.startswith("text/html")
        if not is_logged_out:
            return

        # if we're still logged in we were successful from an authorization POV, so we just need to
        # redo the request in order to return the wanted response to the client
        headers = httpx.Headers({"Accept": "application/json"})
        req_login = httpx.Request(
            "GET",
            URL_ACCOUNTS,
            headers=headers,
        )
        res_login = yield from self._send_through_client(req_login)
        res_login.read()
        is_logged_in = _is_json(res_login)
        if is_logged_in:
            yield from self._send_through_client(request)
            return

        # otherwise we'd need a new authorized session and try again to return the wanted response
        # to the client
        yield from self._sync_auth_flow()
        yield from self._send_through_client(request)

    async def async_auth_flow(
        self,
        request: httpx.Request,
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        # ignore requests to specific resources
        accept = request.headers.get("Accept", "")
        is_specific = accept and accept not in ("*/*", "application/json")
        if is_specific:
            gen = self._send_through_client(request)
            req = next(gen)
            while True:
                res = yield req
                try:
                    req = gen.send(res)
                except StopIteration:
                    break
            return

        # inject headers and try request
        headers = httpx.Headers({"Accept": "application/json"})
        headers.update(request.headers)
        request.headers = headers
        gen = self._send_through_client(request)
        req = next(gen)
        while True:
            res = yield req
            try:
                req = gen.send(res)
            except StopIteration as e:
                res = e.value
                break

        # if we're not logged out we were successful
        content_type = res.headers.get("Content-Type", "")
        is_logged_out = content_type.startswith("text/html")
        if not is_logged_out:
            return

        # if we're still logged in we were successful from an authorization POV, so we just need to
        # redo the request in order to return the wanted response to the client
        headers = httpx.Headers({"Accept": "application/json"})
        req_login = httpx.Request(
            "GET",
            URL_ACCOUNTS,
            headers=headers,
        )
        gen = self._send_through_client(req_login)
        req = next(gen)
        while True:
            res = yield req
            try:
                req = gen.send(res)
            except StopIteration as e:
                res = e.value
                break
        await res.aread()
        is_logged_in = _is_json(res)
        if is_logged_in:
            gen = self._send_through_client(request)
            req = next(gen)
            while True:
                res = yield req
                try:
                    req = gen.send(res)
                except StopIteration:
                    break
            return

        # otherwise we'd need a new authorized session and try again to return the wanted response
        # to the client
        agen = self._async_auth_flow()
        req = await anext(agen)
        while True:
            res = yield req
            try:
                req = await agen.asend(res)
            except StopAsyncIteration:
                break
        gen = self._send_through_client(request)
        req = next(gen)
        while True:
            res = yield req
            try:
                req = gen.send(res)
            except StopIteration:
                break

    def _sync_auth_flow(self) -> Generator[httpx.Request, httpx.Response, None]:
        """Authenticate via SSO"""
        login_id_pre_lock = self._login_id

        with self._lock_sync:
            # we may just have been locked by another concurrent login procedure, that means the
            # cookies just got refreshed and we can return early already
            login_id_post_lock = self._login_id
            if login_id_pre_lock != login_id_post_lock:
                return

            # reset cookies
            self._cookies.clear()

            # resolve authorization
            flow = self._sso_auth()
            req = next(flow)
            while True:
                try:
                    res = yield req
                except httpx.TooManyRedirects as exc:
                    raise SAPLaunchpadAuthUnauthorizedError(
                        "SAP ID Service redirected too many times. "
                        "Please login manually via browser to get more information."
                    ) from exc
                res.read()
                try:
                    req = flow.send(res)
                except StopIteration:
                    break

            # login finished
            self._login_id = uuid4()

    async def _async_auth_flow(self) -> AsyncGenerator[httpx.Request, httpx.Response]:
        """Authenticate via SSO, async variant"""
        login_id_pre_lock = self._login_id

        async with self._lock_async:
            # we may just have been locked by another concurrent login procedure, that means the
            # cookies just got refreshed and we can return early already
            login_id_post_lock = self._login_id
            if login_id_pre_lock != login_id_post_lock:
                return

            # reset cookies
            self._cookies.clear()

            # resolve authorization
            flow = self._sso_auth()
            req = next(flow)
            while True:
                try:
                    res = yield req
                except httpx.TooManyRedirects as exc:
                    raise SAPLaunchpadAuthUnauthorizedError(
                        "SAP ID Service redirected too many times. "
                        "Please login manually via browser to get more information."
                    ) from exc
                await res.aread()
                try:
                    req = flow.send(res)
                except StopIteration:
                    break

            # login finished
            self._login_id = uuid4()

    def _sso_auth(
        self,
    ) -> Generator[httpx.Request, httpx.Response, None]:
        # repeat until we get SAMLResponse to be able to distinguish between the auth methods
        sso_url = httpx.URL(URL_LAUNCHPAD)
        sso_data = dict[str, Any]()
        while "SAMLResponse" not in sso_data and "login_hint" not in sso_data:
            sso_url, sso_data = yield from self._resolve_sso_form(sso_url, sso_data)
            if "changePassword" in str(sso_url):
                raise SAPLaunchpadAuthUnauthorizedError(
                    "SAP ID Service has requested `Change Your Password`, possibly the password is too old. "
                    "Please reset the password manually and try again."
                )

            # if the auth requests user_id and password set it accordingly
            if "j_username" in sso_data:
                sso_data.update(
                    {
                        "j_username": self._user_id,
                        "j_password": self._password,
                    }
                )

        # handle SAML Auth
        if "authn" in str(sso_url):
            yield from self._perform_saml_auth(sso_url, sso_data)
            return

        # handle Gigya Auth
        if "gigya" in str(sso_url):
            yield from self._perform_gigya_auth(sso_url, sso_data)
            return

        raise SAPLaunchpadAuthUnauthorizedError(
            f"Could not determine SSO authorization type from URL: {sso_url}"
        )

    def _resolve_sso_form(
        self,
        url: httpx.URL,
        data: dict[str, Any],
        headers: dict[str, str] | None = None,
        follow_redirects: bool = True,
    ) -> Generator[httpx.Request, httpx.Response, tuple[httpx.URL, dict[str, Any]]]:
        """Fetch SSO form"""
        data_ = data or None

        method = "POST" if data_ is not None else "GET"
        timeout = httpx.Timeout(5)
        extensions = {
            "timeout": timeout.as_dict(),
        }
        req = httpx.Request(
            method,
            url,
            headers=headers,
            data=data_,
            extensions=extensions,
        )
        gen = (
            self._send_through_client_handling_redirects(req, extract_cookies=True)
            if follow_redirects
            else self._send_through_client(req, extract_cookies=True)
        )
        res = yield from gen
        res.raise_for_status()

        endpoint_metadata_tuple = endpoint_metadata_tuple_from_res(res)

        return endpoint_metadata_tuple

    def _perform_saml_auth(
        self,
        url: httpx.URL,
        data: dict[str, Any],
    ) -> Generator[httpx.Request, httpx.Response, None]:
        sso_url, sso_data = yield from self._resolve_sso_form(url, data)

        req = httpx.Request(
            "POST",
            sso_url,
            data=sso_data,
        )
        yield from self._send_through_client_handling_redirects(
            req,
            extract_cookies=True,
        )

    def _perform_gigya_auth(
        self,
        url: httpx.URL,
        data: dict[str, Any],
    ) -> Generator[httpx.Request, httpx.Response, None]:
        gigya_idp_req = httpx.Request(
            "POST",
            url,
            data=data,
        )
        gigya_idp_res = yield from self._send_through_client_handling_redirects(
            gigya_idp_req,
            extract_cookies=True,
        )
        extracted_url_params = re.sub(r"^.*?\?", "", str(gigya_idp_res.url))

        login_url = f"{URL_ACCOUNT_CDC_API}/accounts.webSdkBootstrap"
        login_params = {k: v[0] for k, v in parse_qs(extracted_url_params).items()}
        api_key = login_params["apiKey"]
        login_params.update(
            {
                "pageURL": f"{URL_ACCOUNT_SAML_PROXY}?apiKey={api_key}",
                "sdk": "js_latest",
                "sdkBuild": "12426",
                "format": "json",
            }
        )
        login_req = httpx.Request(
            "GET",
            login_url,
            params=login_params,
            headers=HEADERS_GIGYA,
        )
        yield from self._send_through_client_handling_redirects(
            login_req,
            extract_cookies=True,
        )

        auth_code = yield from self._gigya_auth_code()
        login_token = yield from self._gigya_login_token(login_params, auth_code)

        idp_url = httpx.URL(URL_ACCOUNT_SSO_IDP.format(api_key=api_key))
        idp_data = {
            "loginToken": login_token,
            "samlContext": login_params["samlContext"],
        }
        sso_url, sso_data = yield from self._resolve_sso_form(
            idp_url,
            idp_data,
            follow_redirects=False,
        )

        while not str(sso_url).startswith(URL_LAUNCHPAD):
            sso_url, sso_data = yield from self._resolve_sso_form(
                sso_url,
                sso_data,
                headers=HEADERS_GIGYA,
                follow_redirects=False,
            )

        req = httpx.Request(
            "POST",
            sso_url,
            headers=HEADERS_GIGYA,
            data=sso_data,
        )
        yield from self._send_through_client_handling_redirects(
            req,
            extract_cookies=True,
        )

    def _gigya_auth_code(self) -> Generator[httpx.Request, httpx.Response, str]:
        url = f"{URL_ACCOUNT_CORE_API}/authenticate"
        headers = {
            **HEADERS_GIGYA,
            "Content-Type": "application/json;charset=utf-8",
        }
        params = {
            "reqId": URL_SUPPORT_PORTAL,
        }
        payload = {
            "login": self._user_id,
            "password": self._password,
        }
        req = httpx.Request(
            "POST",
            url,
            params=params,
            headers=headers,
            json=payload,
        )
        res = yield from self._send_through_client_handling_redirects(
            req,
            extract_cookies=True,
        )
        try:
            data = res.json()
        except json.JSONDecodeError as exc:
            raise SAPLaunchpadAuthForbiddenError("Cannot get Gygia auth code") from exc

        auth_code = data["cookieValue"]

        return auth_code

    def _gigya_login_token(
        self,
        login_params: dict[str, Any],
        auth_code: str,
    ) -> Generator[httpx.Request, httpx.Response, str]:
        """Get the Gygia login token"""
        query = "&".join([f"{k}={v}" for k, v in login_params.items()])
        page_url = quote_plus("?".join((URL_ACCOUNT_SAML_PROXY, query)))
        api_key = str(login_params["apiKey"])
        sdk_build = yield from self._gigya_sdk_build(api_key)

        url = f"{URL_ACCOUNT_CDC_API}/socialize.notifyLogin"
        params = {
            "sdk": "js_latest",
            "APIKey": api_key,
            "authMode": "cookie",
            "pageURL": page_url,
            "sdkBuild": sdk_build,
            "format": "json",
            "sessionExpiration": "10",
            "authCode": auth_code,
        }
        req = httpx.Request(
            "GET",
            url,
            params=params,
            headers=HEADERS_GIGYA,
        )
        res = yield from self._send_through_client_handling_redirects(
            req,
            extract_cookies=True,
        )
        data = res.json()
        if data["errorCode"] != 0:
            raise SAPLaunchpadAuthBadGatewayError(
                f"{data['statusCode']} Error: {data['errorMessage']} for url: {res.url}"
            )

        login_token = data["login_token"]

        return login_token

    def _gigya_sdk_build(
        self,
        api_key: str,
    ) -> Generator[httpx.Request, httpx.Response, str]:
        """Get the Gygia SDK build version"""
        url = URL_GIGYA_SDK
        params = {
            "apiKey": api_key,
        }
        req = httpx.Request(
            "GET",
            url,
            params=params,
        )
        res = yield from self._send_through_client_handling_redirects(
            req,
            extract_cookies=True,
        )
        match = re.search(r'gigya.build\s*=\s*{[\s\S]+"number"\s*:\s*(\d+),', res.text)
        if not match:
            raise SAPLaunchpadAuthBadGatewayError(
                "Unable to find gigya sdk build number", res.text
            )

        sdk_build = match.group(1)

        return sdk_build

    def _send_through_client(
        self,
        request: httpx.Request,
        extract_cookies: bool = False,
    ) -> Generator[httpx.Request, httpx.Response, httpx.Response]:
        """Send a single request through the client"""
        # inject headers and cookies
        request.headers.update(HEADERS_COMMON)
        if "Cookie" in request.headers:
            del request.headers["Cookie"]
        self._cookies.set_cookie_header(request)

        # send request through client instance
        res = yield request

        # extract cookies during SSO auth
        if extract_cookies:
            self._cookies.extract_cookies(res)

        return res

    def _send_through_client_handling_redirects(
        self,
        request: httpx.Request,
        extract_cookies: bool = False,
    ) -> Generator[httpx.Request, httpx.Response, httpx.Response]:
        """Handle redirects like the httpx.AsyncClient class"""
        history = list[httpx.Response]()

        while True:
            if len(history) > DEFAULT_MAX_REDIRECTS:
                raise httpx.TooManyRedirects(
                    "Exceeded maximum allowed redirects.",
                    request=request,
                )

            res = yield from self._send_through_client(
                request,
                extract_cookies,
            )
            res.history = list(history)
            if not res.has_redirect_location:
                return res

            history.append(res)
            request = build_redirect_request(request, res)


def _is_json(res: httpx.Response) -> bool:
    """Determine safely if the response is JSON"""
    try:
        res.json()
    except json.JSONDecodeError:
        return False

    return True
