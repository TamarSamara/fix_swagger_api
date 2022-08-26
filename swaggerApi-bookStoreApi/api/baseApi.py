import requests


class BaseApi:
    def __init__(self, url: str, header: dict):
        self._base_url = url
        self.session = requests.session()
        self._headers = {"accept": "application/json"}
        self.session.headers.update(self._headers)
        self.session.headers.update(header)

