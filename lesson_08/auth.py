import requests


base_url = "https://ru.yougile.com/api-v2"
login = "логин"
password = "пароль"


class AuthAPI:
    @staticmethod
    def get_company_id():
        url = base_url + "/auth/companies"
        headers = {'Content-Type': 'application/json'}
        auth_data = {
            "login": login,
            "password": password,
            "name": "New_Test"
        }

        response = requests.post(url, headers=headers, json=auth_data)
        assert response.status_code == 200

        response_data = response.json()
        company_id = response_data["content"][0]["id"]

        return company_id

    def get_token(self):
        company_id = self.get_company_id()
        url = base_url + "/auth/keys"
        headers = {'Content-Type': 'application/json'}
        auth_data = {
            "login": login,
            "password": password,
            "companyId": company_id
        }

        response = requests.post(url, headers=headers, json=auth_data)
        assert response.status_code == 201

        response_data = response.json()
        token = response_data["key"]
        return token
