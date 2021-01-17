import requests

BASIC_URL = "https://dialogs.yandex.net"


class YandexAlice(object):
    def __init__(self, oauth_token):
        self._oauth_token = oauth_token
        self._session = requests.Session()
        self._session.headers.update({'Authorization': f'OAuth {self._oauth_token}'})

    def check_occupied_space(self):
        resp = self._session.get(f"{BASIC_URL}/api/v1/status")
        return resp.text