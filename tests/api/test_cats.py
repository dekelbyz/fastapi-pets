from fastapi.testclient import TestClient
from pets.dto import AnimalType
from server import app
import pytest
import random
import string

client = TestClient(app)

class TestPet:

    @classmethod
    def setup_class(cls):
        cls.headers = {"Content-Type": "application/json"}
        cls.base_endpoint = '/pets/'

    @pytest.mark.parametrize("animal_type,expected", [(key.value, 201) for key in AnimalType])
    def test_add_pet(self, animal_type, expected):
        payload = {'animal_type': animal_type, 'name': ''.join(
            random.choice(string.ascii_lowercase) for i in range(11))}
        response = client.post(
            self.base_endpoint, headers=self.headers, json=payload)
        assert response.status_code == expected
