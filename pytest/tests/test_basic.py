import pytest
import httpx


class TestBasicAPI:

    BASE_URL = "https://swapi.info/api"

    def test_api_is_accessible(self):
        response = httpx.get(f"{self.BASE_URL}/people/")
        assert response.status_code == 200

        print(response.status_code)

    def test_negative_id_returns_error(self, api_client):
        response = httpx.get(f"{self.BASE_URL}/people/-1/")
        assert response.status_code != 200

        print(response.status_code)

    def response_headers(self, api_client):
        response = httpx.get(f"{self.BASE_URL}/people/1")
        headers = response.headers

        print(response.headers)

        assert "Content-Type" in headers
        assert "application/json" in headers["Content-Type"]