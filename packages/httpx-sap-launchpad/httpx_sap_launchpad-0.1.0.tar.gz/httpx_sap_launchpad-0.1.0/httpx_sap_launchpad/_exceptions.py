class SAPLaunchpadAuthError(Exception):
    """Base httpx SAP Launchpad error"""


class SAPLaunchpadAuthUnauthorizedError(SAPLaunchpadAuthError):
    """httpx SAP Launchpad unauthorized error"""


class SAPLaunchpadAuthForbiddenError(SAPLaunchpadAuthError):
    """httpx SAP Launchpad forbidden error"""


class SAPLaunchpadAuthBadGatewayError(SAPLaunchpadAuthError):
    """httpx SAP Launchpad bad gateway error"""
