import requests

BASIC_URL = "https://dialogs.yandex.net"
GEOLOCATION_ALLOWED = 'Geolocation.Allowed'
GEOLOCATION_REJECTED = 'Geolocation.Rejected'


class YandexAlice(object):
    def __init__(self, oauth_token, skill_id):
        self._oauth_token = oauth_token
        self._skill_id = skill_id
        self._session = requests.Session()
        self._session.headers.update({'Authorization': f'OAuth {self._oauth_token}'})

    def check_occupied_space(self) -> dict:
        resp = self._session.get(f"{BASIC_URL}/api/v1/status")
        return resp.json()

    def upload_image_via_link(self, image_link: str) -> dict:
        resp = self._session.post(url=f"{BASIC_URL}/api/v1/skills/{self._skill_id}/images", data={"url": image_link})
        return resp.json()

    def get_list_of_images(self) -> dict:
        resp = self._session.get(f"{BASIC_URL}/api/v1/skills/{self._skill_id}/images")
        return resp.json()

    def delete_image(self, image_id: str) -> dict:
        resp = self._session.delete(f"{BASIC_URL}/api/v1/skills/{self._skill_id}/images/{image_id}")
        return resp.json()

    @staticmethod
    def create_image(image_id: str, title: str, description: str):
        return {
            'type': 'BigImage',
            'image_id': image_id,
            'title': title,
            'description': description
        }

    @staticmethod
    def create_image_gallery(image_ids: list) -> dict:
        items = [{'image_id': image_id} for image_id in image_ids]
        return {
            'type': 'ImageGallery',
            'items': items
        }

    @staticmethod
    def create_button(title: str, payload=None, url=None, hide=False) -> dict:
        button = {
            'title': title,
            'hide': hide
        }
        if payload is not None:
            button['payload'] = payload
        if url is not None:
            button['url'] = url
        return button

    @staticmethod
    def check_location(event):
        return event['session'].get('location') is not None

