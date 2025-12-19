from typing import List

EXPECTED_CHARACTER_FIELDS = [
    'name', 'height', 'mass', 'hair_color', 'skin_color',
    'eye_color', 'birth_year', 'gender', 'homeworld',
    'films', 'species', 'vehicles', 'starships', 'created',
    'edited', 'url'
]

CHARACTER_TEST_DATA = [
    (1, "Luke Skywalker"),
    (2, "C-3PO"),
    (3, "R2-D2"),
    (4, "Darth Vader"),
]

def validate_response_structure(data: dict, expected_fields: List[str]) -> bool:
    return all(field in  data for field in expected_fields)