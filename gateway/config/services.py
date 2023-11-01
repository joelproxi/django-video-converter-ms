import json
import requests
from config import settings


class RemoteService:
    def __init__(self, request, entity_name: str, version: str) -> None:
        self.request = request
        self.version = version
        self.entity_name = entity_name
        self.url = f"{settings.ENTITY_URL_MAP.get(entity_name)}/api/{version}/{entity_name}"

    def _get_headers(self, new_headers=None):
        base_headers = {
            'content-type': 'application/json'
        }
        new_headers = new_headers or {}
        return {
            **self.request.headers,
            **new_headers,
            **base_headers
        }


class AuthService(RemoteService):
    def __init__(self, request) -> None:
        super().__init__(request, 'auth', 'v1')

    def authenticate(self, entity_data, path=''):
        print(f"{self.url}/{path}")
        return requests.post(
            f"{self.url}/{path}",
            data=json.dumps(entity_data),
            headers=self._get_headers())

    def get_user_info(self, path=''):
        return requests.get(
            f"{self.url}/{path}",
            headers=self._get_headers()
        )
