import pytest
from utils.api_client import SWAPIClient

@pytest.fixture
def api_client():
    client = SWAPIClient()
    yield client
    client.close()

@pytest.fixture
def base_url():
    return "https://swapi.info/api"