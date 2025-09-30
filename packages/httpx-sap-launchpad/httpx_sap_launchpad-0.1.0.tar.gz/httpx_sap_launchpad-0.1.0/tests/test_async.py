import httpx
import pytest

from httpx_sap_launchpad import SAPLaunchpadAuth, URL_LAUNCHPAD

from ._mock import mock_async, USER_ID, PASSWORD


@pytest.mark.asyncio
async def test_login() -> None:
    auth = SAPLaunchpadAuth(
        user_id=USER_ID,
        password=PASSWORD,
    )
    req = httpx.Request(
        method="GET",
        url=f"{URL_LAUNCHPAD}/applications/softwarecenter/version.json",
    )
    requests, response = await mock_async(auth, req)

    assert len(requests) == 8
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
