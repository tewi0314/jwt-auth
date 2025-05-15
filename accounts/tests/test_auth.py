# accounts/tests/test_auth.py

import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_login_fail_wrong_password():
    client = APIClient()

    client.post("/signup", {
        "username": "jinho",
        "password": "1234",
        "nickname": "mentos"
    }, format="json")

    response = client.post("/login", {
        "username": "jinho",
        "password": "wrong"
    }, format="json")

    print("RESPONSE:", response.status_code, response.data)

    assert response.status_code == 401
    assert response.data["error"]["code"] == "INVALID_CREDENTIALS"


