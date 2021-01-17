import requests

BASIC_URL = "https://dialogs.yandex.net"


class YandexAlice(object):
    def __init__(self, oauth_token, skill_id):
        self._oauth_token = oauth_token
        self._skill_id = skill_id
        self._session = requests.Session()
        self._session.headers.update({'Authorization': f'OAuth {self._oauth_token}'})

    def check_occupied_space(self) -> dict:
        resp = self._session.get(f"{BASIC_URL}/api/v1/status")
        return resp.text

    def upload_image_via_link(self, image_link: str) -> dict:
        resp = self._session.post(url=f"{BASIC_URL}/api/v1/skills/{self._skill_id}/images", data={"url": image_link})
        return resp.text

    def get_list_of_images(self) -> dict:
        resp = self._session.get(f"{BASIC_URL}/api/v1/skills/{self._skill_id}/images")
        return resp.text

    def delete_image(self, image_id: str) -> dict:
        resp = self._session.delete(f"{BASIC_URL}/api/v1/skills/{self._skill_id}/images/{image_id}")
        return resp.text
