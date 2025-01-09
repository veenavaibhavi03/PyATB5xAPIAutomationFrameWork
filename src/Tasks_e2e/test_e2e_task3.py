#create booking -> update booking -> patch

import allure
import pytest
from requests import Response

from src.Constants.api_constants import APIConstants
from src.Helpers.api_requests_wrapper import put_request, delete_request, post_request, patch_request
from src.Helpers.common_verification import verify_response_key, verify_HTTP_status_code, verify_json_key_gr_zero, \
    verify_delete_response, verify_json_key_not_none
from src.Helpers.payload_manager import payload_update_booking, payload_create_booking
from src.utils.utils import utils

class Test_e2e(object):
    @pytest.mark.positive
    @allure.title("Create a booking")
    @allure.description("Verify that a valid booking is created")
    def test_createABooking(self):
        create_booking=post_request(
            URl=APIConstants.url_create_booking(self),
            pay_load=payload_create_booking(),
            Auth=None,
            Headers=utils.common_headers_json(self),
            in_jsonResponse=False
        )

        #print(create_booking.json())
        verify_HTTP_status_code(create_booking,200)
        verify_json_key_not_none(create_booking.json()["bookingid"])
        #print(create_booking.json()["booking"]["firstname"])
        verify_response_key(create_booking.json()["booking"]["firstname"],"Jim")


    @pytest.mark.positive
    def test_booking_patch_request(self,createToken,get_booking_id):
        patch_url= APIConstants.url_patch_put_delete(get_booking_id)
        patch_response=patch_request(
            URl=patch_url,
            pay_load=payload_update_booking(),
            Auth=None,
            in_jsonResponse=False,
            Headers=utils.common_header_put_patch_delete_basic_cookie(self,createToken)

        )
        verify_HTTP_status_code(patch_response,200)
        verify_response_key(patch_response.json()["firstname"],"Marina")



