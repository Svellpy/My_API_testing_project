import pytest

class TestPerformance:

    def test_responce_time(self, api_client):
        response_time = api_client.measure_response_time("/people/1/")
        assert response_time < 2.0

    @pytest.mark.parametrize("endpoint", [
        "/people/1/",
        "/people/2/",
        "/people/3/",
    ])
    def test_multiple_endpoints_response_time(self, api_client, endpoint):
        response_time = api_client.measure_response_time(endpoint)
        assert response_time < 3.0