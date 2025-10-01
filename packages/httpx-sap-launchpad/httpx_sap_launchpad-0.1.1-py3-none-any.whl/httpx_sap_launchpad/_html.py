from typing import Any
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag
import httpx

from ._exceptions import (
    SAPLaunchpadAuthBadGatewayError,
    SAPLaunchpadAuthUnauthorizedError,
)


def endpoint_metadata_tuple_from_res(
    res: httpx.Response,
) -> tuple[httpx.URL, dict[str, Any]]:
    soup = BeautifulSoup(res.text, features="html.parser")

    error_message = soup.find("div", {"id": "globalMessages"})
    if error_message and "we could not authenticate you" in error_message.text:
        raise SAPLaunchpadAuthUnauthorizedError(
            "Authentication failed, bad user_id or password"
        )

    form = soup.find("form")
    if not isinstance(form, Tag):
        raise SAPLaunchpadAuthBadGatewayError(
            f"Unable to find form: {res.url}\nContent:\n{res.text}"
        )

    action = str(form["action"])
    endpoint = httpx.URL(urljoin(str(res.url), action))
    metadata = dict(
        (i["name"], i.get("value"))
        for i in form.find_all("input")
        if i.get("type") != "submit" and i.get("name")
    )

    return endpoint, metadata
