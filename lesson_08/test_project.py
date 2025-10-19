import requests
from auth import AuthAPI

base_url = "https://ru.yougile.com/api-v2"


class TestProjects:
    def setup_method(self):
        self.auth = AuthAPI()
        self.token = self.auth.get_token()
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.token
        }

    def _create_project(self, title):
        url = base_url + "/projects"
        project_data = {"title": title}
        response = requests.post(
            url,
            headers=self.headers,
            json=project_data
        )
        return response.json()["id"]

    def test_create_project(self):
        self._create_project("Big_Sky")

    def test_create_project_negative_empty_title(self):
        url = base_url + "/projects"
        project_data = {"title": ""}
        response = requests.post(
            url,
            headers=self.headers,
            json=project_data
        )
        assert response.status_code == 400

    def test_change_project(self):
        project_id = self._create_project("Project_to_change")

        url_change = base_url + "/projects/" + project_id
        change_title = {"title": "New_SkyPro"}
        response = requests.put(
            url_change,
            headers=self.headers,
            json=change_title
        )
        assert response.status_code == 200

    def test_change_project_negative(self):
        url_change = base_url + "/projects/" + '564312354'
        change_title = {"title": "Invalid_id"}
        response = requests.put(
            url_change,
            headers=self.headers,
            json=change_title
        )
        assert response.status_code == 404

    def test_get_description(self):
        project_id = self._create_project("For_descript")

        url_get = base_url + "/projects/" + project_id
        response = requests.get(url_get, headers=self.headers)
        assert response.status_code == 200

        response_data = response.json()
        assert response_data["id"] == project_id
        assert response_data["title"] == "For_descript"

    def test_get_description_negative(self):
        url_get = base_url + "/projects/" + "bug"
        response = requests.get(url_get, headers=self.headers)
        assert response.status_code == 404
