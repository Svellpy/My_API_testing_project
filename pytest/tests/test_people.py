import pytest
from utils.helpers import EXPECTED_CHARACTER_FIELDS, CHARACTER_TEST_DATA
from utils.api_client import SWAPIClient

class TestSWAPIPeopleAPI:

    def test_get_specific_character(self, api_client: SWAPIClient):
        data = api_client.get_character(1)
        assert data["name"] == "Luke Skywalker"

    @pytest.mark. parametrize("character_id, expected_name", CHARACTER_TEST_DATA)
    def test_multiple_characters(self, api_client: SWAPIClient,
                                character_id: int, expected_name: str):
        data = api_client.get_character(character_id)
        assert data["name"] == expected_name

    def test_response_structere(self, api_client: SWAPIClient):
        character = api_client.get_character(1)

        if character.get("homeworld"):
            homeworld = api_client.get_resource(character["homeworld"])
            assert "name" in homeworld
            assert "climate" in homeworld