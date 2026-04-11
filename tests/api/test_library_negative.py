import pytest
from src.api.api_endpoint import Endpoints
from src.api.api_payloads import add_book_payload
from src.api.api_assertions import APIAssertion


@pytest.mark.api
@pytest.mark.negative
def test_add_book_missing_field(api_client):

    payload = {
        "name": "Test Book",
        "isbn": "",
        "author": "Test Author"
    }

    response = api_client.post(Endpoints.ADD_BOOK, json=payload)

    APIAssertion.assert_status_code(response, 404)


@pytest.mark.api_negative
def test_add_duplicate_book(api_client):

    payload, _ = add_book_payload()

    api_client.post(Endpoints.ADD_BOOK, json=payload)

    response = api_client.post(Endpoints.ADD_BOOK, json=payload)

    APIAssertion.assert_in("already exists", response.text)



@pytest.mark.api_negative
def test_get_invalid_book(api_client):

    response = api_client.get(Endpoints.GET_BOOK, params={"ID": "invalid123"})

    data = response.json()

    assert data == []


@pytest.mark.api_negative
def test_delete_invalid_book(api_client):

    response = api_client.delete(
        Endpoints.DELETE_BOOK,
        json={"ID": "invalid123"}
    )

    APIAssertion.assert_in("does not exists", response.text)