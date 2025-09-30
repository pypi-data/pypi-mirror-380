# https://github.com/sap-linuxlab/community.sap_launchpad/blob/main/plugins/module_utils/constants.py
URL_ACCOUNT = "https://account.sap.com"
URL_ACCOUNTS = "https://accounts.sap.com"
URL_LAUNCHPAD = "https://launchpad.support.sap.com"

# Gigya Auth
URL_ACCOUNT_CDC_API = "https://cdc-api.account.sap.com"
URL_ACCOUNT_CORE_API = "https://core-api.account.sap.com/uid-core"
URL_ACCOUNT_SAML_PROXY = f"{URL_ACCOUNT}/core/SAMLProxyPage.html"
URL_ACCOUNT_SSO_IDP = f"{URL_ACCOUNT_CDC_API}/saml/v2.0/{{api_key}}/idp/sso/continue"
URL_GIGYA_SDK = "https://cdns.gigya.com/js/gigya.js"
URL_SUPPORT_PORTAL = "https://hana.ondemand.com/supportportal"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/72.0.3626.109 Safari/537.36"
)

HEADERS_COMMON = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": USER_AGENT,
}
HEADERS_GIGYA = {
    **HEADERS_COMMON,
    "Origin": URL_ACCOUNTS,
    "Referer": URL_ACCOUNTS,
    "Accept": "*/*",
}
