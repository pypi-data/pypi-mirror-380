from lxml import html
from urllib.parse import urlparse, parse_qs
from .InsulaOpenIDConnect import InsulaOpenIDConnect


class AscendOpenIDConnect(InsulaOpenIDConnect):

    def __retrieve_authorization_from_endpoint(self) -> str:
        """
        Calls the authorization endpoint and returns 'code'
        For the Ascend keycloak instance, the correct code to retrieve the token is given at the second login redirect call.
        Not at the first like for other Insula instances.
        """
        get_params = {
            "client_id": self.__client_id,
            "redirect_uri": self.__redirect_uri,
            "scope": "openid",
            "response_type": "code"
        }

        response_auth = self.__session.get(url=self.__authorization_endpoint, params=get_params, timeout=(4100, 400))
        if response_auth.status_code != 200:
            self.__logs_and_raise('call authorization endpoint failed')

        auth_url = html.fromstring(response_auth.content.decode()).forms[0].action

        post_data = {
            "username": self.__username,
            "password": self.__password
        }

        response_login = self.__session.post(auth_url, data=post_data, allow_redirects=False, timeout=(4100, 400))

        if response_login.status_code != 302:
            self.__logs_and_raise('Authorization failed, username or password incorrect [err: 199]')

        if 'Location' not in response_login.headers:
            self.__logs_and_raise('Authorization failed, username or password incorrect [err: 100]')

        redirect_auth_url = response_login.headers['Location']
        response_login_redirect = self.__session.get(redirect_auth_url, allow_redirects=False, timeout=(4100, 400))

        if response_login_redirect.status_code > 400:
            self.__logs_and_raise('Authorization failed, username or password incorrect [err: 199]')

        return parse_qs(urlparse(response_login_redirect.headers['Location']).query)['code'][0]
