from http import HTTPStatus

import httpx


def build_redirect_request(
    req: httpx.Request,
    res: httpx.Response,
) -> httpx.Request:
    """Util copied straight from httpx.AsyncClient"""
    method = _redirect_method(req, res)
    url = _redirect_url(req, res)
    headers = _redirect_headers(req, url, method)
    stream = _redirect_stream(req, method)

    return httpx.Request(
        method=method,
        url=url,
        headers=headers,
        stream=stream,
        extensions=req.extensions,
    )


def _redirect_method(
    req: httpx.Request,
    res: httpx.Response,
) -> str:
    """Util copied straight from httpx.AsyncClient"""
    method = req.method

    # https://tools.ietf.org/html/rfc7231#section-6.4.4
    if res.status_code == HTTPStatus.SEE_OTHER.value and method != "HEAD":
        method = "GET"

    # Do what the browsers do, despite standards...
    # Turn 302s into GETs.
    if res.status_code == HTTPStatus.FOUND.value and method != "HEAD":
        method = "GET"

    # If a POST is responded to with a 301, turn it into a GET.
    # This bizarre behaviour is explained in 'requests' issue 1704.
    if res.status_code == HTTPStatus.MOVED_PERMANENTLY.value and method == "POST":
        method = "GET"

    return method


def _redirect_url(
    req: httpx.Request,
    res: httpx.Response,
) -> httpx.URL:
    """Util copied straight from httpx.AsyncClient"""
    location = res.headers["Location"]

    try:
        url = httpx.URL(location)
    except httpx.InvalidURL as exc:
        raise httpx.RemoteProtocolError(
            f"Invalid URL in location header: {exc}.",
            request=req,
        ) from None

    # Handle malformed 'Location' headers that are "absolute" form, have no host.
    # See: https://github.com/encode/httpx/issues/771
    if url.scheme and not url.host:
        url = url.copy_with(host=req.url.host)

    # Facilitate relative 'Location' headers, as allowed by RFC 7231.
    # (e.g. '/path/to/resource' instead of 'http://domain.tld/path/to/resource')
    if url.is_relative_url:
        url = req.url.join(url)

    # Attach previous fragment if needed (RFC 7231 7.1.2)
    if req.url.fragment and not url.fragment:
        url = url.copy_with(fragment=req.url.fragment)

    return url


def _redirect_headers(
    req: httpx.Request,
    url: httpx.URL,
    method: str,
) -> httpx.Headers:
    """Util copied straight from httpx.AsyncClient"""
    headers = httpx.Headers(req.headers)

    if not _same_origin(url, req.url):
        if not _is_https_redirect(req.url, url):
            # Strip Authorization headers when responses are redirected
            # away from the origin. (Except for direct HTTP to HTTPS redirects.)
            headers.pop("Authorization", None)

        # Update the Host header.
        headers["Host"] = url.netloc.decode("ascii")

    if method != req.method and method == "GET":
        # If we've switch to a 'GET' request, then strip any headers which
        # are only relevant to the request body.
        headers.pop("Content-Length", None)
        headers.pop("Transfer-Encoding", None)

    # We should use the client cookie store to determine any cookie header,
    # rather than whatever was on the original outgoing request.
    headers.pop("Cookie", None)

    return headers


def _redirect_stream(
    req: httpx.Request,
    method: str,
) -> httpx.SyncByteStream | httpx.AsyncByteStream | None:
    """Util copied straight from httpx.AsyncClient"""
    if method != req.method and method == "GET":
        return None

    return req.stream


def _is_https_redirect(
    url: httpx.URL,
    location: httpx.URL,
) -> bool:
    """Util copied straight from httpx.AsyncClient"""
    if url.host != location.host:
        return False

    return (
        url.scheme == "http"
        and _port_or_default(url) == 80
        and location.scheme == "https"
        and _port_or_default(location) == 443
    )


def _same_origin(url: httpx.URL, other: httpx.URL) -> bool:
    """Util copied straight from httpx.AsyncClient"""
    return (
        url.scheme == other.scheme
        and url.host == other.host
        and _port_or_default(url) == _port_or_default(other)
    )


def _port_or_default(url: httpx.URL) -> int | None:
    """Util copied straight from httpx.AsyncClient"""
    if url.port is not None:
        return url.port

    return {"http": 80, "https": 443}.get(url.scheme)
