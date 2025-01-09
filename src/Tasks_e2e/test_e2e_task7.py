#Trying to update without token
import allure
import pytest
from requests import Response

from src.Constants.api_constants import APIConstants
from src.Helpers.api_requests_wrapper import put_request, delete_request
from src.Helpers.common_verification import verify_response_key, verify_HTTP_status_code, verify_json_key_gr_zero, \
    verify_delete_response
from src.Helpers.payload_manager import payload_update_booking
from src.utils.utils import utils

class Test_E2E_(object):
    @pytest.mark.positive
    @allure.title("E2E-createBooking->Update-> Delete")
    @allure.description("verify the response of created booking id with invalid payload")
    def test_update_booking_with_invalid_payload(self, createToken, get_booking_id):
        # print(createToken,get_booking_id)
        BookingId = get_booking_id
        _token = createToken
        put_url = APIConstants.url_patch_put_delete(booking_id=BookingId)
        # print(put_url)
        Put_response = put_request(
            # (URl: Any,Auth: Any,pay_load: Any,Headers: Any,in_jsonResponse: {__eq__}) -> Response
            URl=put_url,
            Headers=utils.common_header_put_patch_delete_basic_cookie(self, token=_token),
            Auth=None,
            pay_load={},
            in_jsonResponse=False

        )
        # print(Put_response.json()["firstname"])

        verify_HTTP_status_code(Put_response, 400)

