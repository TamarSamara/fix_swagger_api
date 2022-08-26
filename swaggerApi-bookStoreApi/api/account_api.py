from api.baseApi import BaseApi


class AccountApi(BaseApi):
    def __init__(self, url: str, header: dict):
        super().__init__(url, header)
        self._url = f"{self._base_url}Account/v1"

    def post_account_user(self, user):
        res = self.session.post(f"{self._url}/User", json=user)
        return res

    def delete_user(self, uid: str):
        res = self.session.get(url=f"{self._url}User/{uid}", headers=self._headers)
        return res

    def get_user(self, uid: str):
        res = self.session.get(url=f"{self._url}User/{uid}", headers=self._headers)
        return res

    def post_login_authorized(self, login):
        res = self.session.post(url=f"{self._url}/Authorized", data=login)
        return res

    def post_login_account_generate_token(self, login):
        res = self.session.post(f"{self._url}/GenerateToken", data=login)
        return res

    def post_login_account_generate_token2(self, login):
        res = self.session.post(url=f"{self._url}/GenerateToken", data=login)
        return res


