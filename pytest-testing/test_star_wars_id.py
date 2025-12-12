import httpx
import pytest


url = "https://swapi.dev/api/people/"

response = httpx.get(url)
print(response)

data = response.json()
print(data)

status_code = response.status_code
print(status_code)

def test_api_is_accessible():
    response = httpx.get(url)
    assert response.status_code == 200

def test_get_specific_character():
    response = httpx.get(f"{url}1/")
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Luke Skywalker"
    assert "films" in data
    assert "homeworld" in data
    assert "starships" in data

def test_invalid_character_id():
    response = httpx.get(f"{url}900/")

    assert response.status_code == 404

def test_response_structure():
    response = httpx.get(f"{url}4/")
    data = response.json()
    expected_fields = [
        'name', 'height', 'mass', 'hair_color', 'skin_color',
        'eye_color', 'birth_year', 'gender', 'homeworld',
        'films', 'species', 'vehicles', 'starships', 'created',
        'edited', 'url'
    ]
    for fields in expected_fields:
        assert fields in data

# Тесты с параметризацией 

@pytest.mark.parametrize("character_id, expected_name", [
    (1, "Luke Skywalker"),
    (2, "C-3PO"),
    (3, "R2-D2"),
    (4, "Darth Vader"),
])

def test_multiple_characters(character_id, expected_name):
    response = httpx.get(f"{url}{character_id}/")
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == expected_name

def test_nex_page():
    response = httpx.get(url)
    first_page = response.json()

    if first_page["next"]:
        next_response = httpx.get(first_page["next"])
        second_page = next_response.json()

        assert next_response.status_code == 200
        assert "results" in second_page
        assert len(second_page["results"]) > 0