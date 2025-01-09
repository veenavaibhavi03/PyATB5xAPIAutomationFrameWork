#Get A BookingId -> Delete-> verify
import allure
import pytest
from requests import Response

from conftest import createToken
from src.Constants.api_constants import APIConstants
from src.Helpers.api_requests_wrapper import put_request, delete_request, get_request
from src.Helpers.common_verification import verify_response_key, verify_HTTP_status_code, verify_json_key_gr_zero, \
    verify_delete_response
from src.Helpers.payload_manager import payload_update_booking
from src.utils.utils import utils

@pytest.mark.positive
@allure.title("Fetch the created booking and delete it")
@allure.description("verify that using valid bookingId the response can be fetched and also can be deleted.")
def test_get_a_booking(get_booking_id,createToken):
    get_url=APIConstants.url_patch_put_delete(get_booking_id)
    _token=createToken
    get_response=get_request(
        Url=get_url,
        auth=None,
        in_jsonResponse=False

    )
    verify_HTTP_status_code(get_response,200)
    verify_response_key(get_response.json()["firstname"],"Jim")
    delete_response=delete_request(
        URl=get_url,
        Headers=utils().common_header_put_patch_delete_basic_cookie(_token),
        Auth=None,
        in_jsonResponse=False
    )
    verify_HTTP_status_code(delete_response,201)
    verify_delete_response(delete_response.text)

