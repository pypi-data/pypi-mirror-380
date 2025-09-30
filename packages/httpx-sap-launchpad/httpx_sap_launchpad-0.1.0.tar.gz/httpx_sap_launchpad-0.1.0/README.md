# httpx-sap-launchpad

This library provides [httpx](https://www.python-httpx.org/) [Authentication](https://www.python-httpx.org/advanced/authentication/) for the _SAP Launchpad API_, primarily focusing on downloading software and files from the _SAP_ _Software Download Center_ and _Maintenance Planner_.

This library is not affiliated with _SAP_ in any way.

> ⚠️ **Warning**: This library is not verified to work as I don't have access to an SAP account anymore. If problems are to be discovered I'd be happy to provide guidance and fixes, but that also means I'd need credentials to replicate the issue.

## Install

Install with your package manager of choice:

```shell
pip install httpx-sap-launchpad
```

## Usage

`SAPLaunchpadAuth` extends the `httpx.Auth` class, so the usage is simple:

```python
import httpx
from httpx_sap_launchpad import URL_LAUNCHPAD, SAPLaunchpadAuth


def main() -> None:
    auth = SAPLaunchpadAuth(
        user_id='S1234567890',
        password='password',
    )
    httpx.get(f'{URL_LAUNCHPAD}/applications/softwarecenter/version.json', auth=auth)


if __name__ == '__main__':
    main()
```

`SAPLaunchpadAuth` can be used in conjunction with a `Client` in order to
make use of connection pooling:

```python
import httpx
from httpx_sap_launchpad import URL_LAUNCHPAD, SAPLaunchpadAuth


def main() -> None:
    auth = SAPLaunchpadAuth(
        user_id='S1234567890',
        password='password',
    )
    with httpx.Client(auth=auth) as client:
        client.get(f'{URL_LAUNCHPAD}/applications/softwarecenter/version.json')


if __name__ == '__main__':
    main()
```

...or the `AsyncClient`:

```python
import asyncio

import httpx
from httpx_sap_launchpad import URL_LAUNCHPAD, SAPLaunchpadAuth


async def main() -> None:
    auth = SAPLaunchpadAuth(
        user_id='S1234567890',
        password='password',
    )
    async with httpx.AsyncClient(auth=auth) as client:
        await client.get(f'{URL_LAUNCHPAD}/applications/softwarecenter/version.json')


if __name__ == '__main__':
    asyncio.run(main())
```

## Credit

The authorization flow is based on the [community.sap_launchpad](https://github.com/sap-linuxlab/community.sap_launchpad) _Ansible_ collection.

## License

**MIT** - **wh!le (whilenot-dev)**, see [LICENSE](./LICENSE.txt)
