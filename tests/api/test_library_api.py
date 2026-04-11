import pytest
from src.api.api_endpoint import Endpoints
from src.api.api_payloads import add_book_payload
from src.api.api_assertions import APIAssertion
from src.api.api_logger import logger


@pytest.mark.api
def test_library_api_flow(api_client):

    payload, book_id = add_book_payload()

    # ADD
    add_response = api_client.post(Endpoints.ADD_BOOK, json=payload)

    APIAssertion.assert_status_code(add_response, 200)
    APIAssertion.assert_json_value(add_response, "Msg", "successfully added")

    # GET
    get_response = api_client.get(Endpoints.GET_BOOK, params={"ID": book_id})

    APIAssertion.assert_status_code(get_response, 200)

    data = get_response.json()

    APIAssertion.assert_not_empty(data)
    logger.info(f"the api response is {data}")
    APIAssertion.assert_equal(data[0]["isbn"], payload["isbn"], "ISBN mismatch")
    APIAssertion.assert_equal(data[0]["aisle"], payload["aisle"], "Aisle mismatch")

    # DELETE
    delete_response = api_client.delete(
        Endpoints.DELETE_BOOK,
        json={"ID": book_id}
    )

    APIAssertion.assert_status_code(delete_response, 200)
    APIAssertion.assert_in("successfully deleted", delete_response.text)