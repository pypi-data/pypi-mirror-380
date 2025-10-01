import os

from lsrestclient.auth import auth_am_login_apikey


def test_auth_am_login_apikey():
    os.environ["AM_API_URL"] = "https://am.lsoft.online/api/v2/am"
    am_auth_token = auth_am_login_apikey(
        org_id="ESO-2k8mJKQ2BA", api_key="ESAAK-VZ7k1oYq9wdL9v5Jr260vejPXgEBG3Q6"
    )
    print(am_auth_token)
