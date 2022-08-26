import requests
from models.user import User


class UserApi:
    def __init__(self, url: str = "https://petstore3.swagger.io/api/v3/user"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def post_new_user(self, my_user) -> User or int:
        my_user_data = my_user.to_json()
        res = self._session.post(url=f"{self._url}", data=my_user_data, headers=self._headers)
        if res.status_code == 200:
            u1 = User(**res.json())
            return u1
        else:
            return res.status_code

    def post_list_of_new_users(self, user_list: [User]) -> [User] or int:
        ulist = []
        res = self._session.post(url=f"{self._url}/createWithList", data=user_list, headers=self._headers)
        if res.status_code == 200:
            res = res.json()
            for user in res:
                u1 = User(**user)
                ulist.append(u1)
                return ulist
        else:
            return res.status_code

    def get_user_login(self, usernamepassword: str):
        res = self._session.get(f"{self._url}/login", params=usernamepassword, headers=self._headers)
        if res.status_code == 200:
            return res.content.__str__()
        else:
            return res.status_code

    def get_user_logout(self) -> str or int:
        res = self._session.get(f"{self._url}/logout")
        if res.status_code == 200:
            return res
        else:
            return res.status_code

    def get_user_by_username(self, username) -> User or int:
        res = self._session.get(f"{self._url}/{username}", headers=self._headers)
        return res

    def put_user(self, username: str) -> User or int:
        res = self._session.put(f"{self._url}/{username}", headers=self._headers)
        if res.status_code == 200:
            u1 = User(**res.json())
            return u1
        else:
            return res.status_code

    def delete_user(self, username) -> User or int:
        res = self._session.delete(f"{self._url}/{username}", headers=self._headers)
        if res.status_code == 200:
            res = self._session.get(f"{self._url}/{username}", headers=self._headers)
            if res.status_code == 200:
                u1 = User(**res.json())
                return u1
            else:
                return res.status_code
