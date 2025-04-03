# Reason to reuse the create token and create booking.
# this file will be first executed by the pytest
# we can keep the logic or code which we want to execute before making the test request.
import pytest
import allure
from src.Helpers.api_requests_wrapper import  *
from src.Helpers.payload_manager import *
from src.Helpers.common_verification import *
from src.Constants.api_constants import *
from src.utils.utils import  *

@pytest.fixture(scope="session")
def createToken():
    Response=post_request(
        URl=APIConstants().url_create_token(),
        Auth=None,
        pay_load=create_token_auth(),
        Headers=utils().common_headers_json(),
        in_jsonResponse=False
    )
    """print(APIConstants().url_create_token())
    print(create_token_auth())
    print(utils().common_headers_json())"""
    verify_HTTP_status_code(response_data=Response,expected_data=200)
    verify_json_key_not_none(Response.json()["token"])
    return Response.json()["token"]

@pytest.fixture(scope="session")
def get_booking_id():
    Response = post_request(
        URl=APIConstants().url_create_booking(),
        Auth=None,
        pay_load=payload_create_booking(),
        Headers=utils().common_headers_json(),
        in_jsonResponse=False
    )
    #print(Response.json()["bookingid"])
    bookId= Response.json()["bookingid"]
    verify_HTTP_status_code(response_data=Response, expected_data=200)
    verify_json_key_not_none(bookId)
    return bookId


#get_booking_id()
