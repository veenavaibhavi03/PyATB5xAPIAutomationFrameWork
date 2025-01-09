#create booking ->Delete it -> verify
from wsgiref.headers import Headers

import allure
import pytest
from requests import Response

from src.Constants.api_constants import APIConstants
from src.Helpers.api_requests_wrapper import put_request, delete_request, post_request
from src.Helpers.common_verification import verify_response_key, verify_HTTP_status_code, verify_json_key_gr_zero, \
    verify_delete_response, verify_json_key_not_none
from src.Helpers.payload_manager import payload_update_booking, payload_create_booking
from src.utils.utils import utils

class Test_E2E(object):
    @pytest.mark.positive
    @allure.title("Create a booking")
    @allure.description("Verify that a valid booking is created")
    def test_create_a_booking(self):
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
    @allure.title("Delete a booking and verifying the update request for deleted ID")
    @allure.description("Verify that a booking is deleted when the booking id is passed and also"
                        "check the update request for deleted Id")
    def test_delete_a_booking(self,createToken,get_booking_id):
        print(createToken, get_booking_id)
        delete_url = APIConstants.url_patch_put_delete(booking_id=get_booking_id)
        print(delete_url)
        # URl,Auth,pay_load,Headers,in_jsonResponse
        delete_response = delete_request(
            URl=delete_url,
            Auth=None,
            Headers=utils.common_header_put_patch_delete_basic_cookie(self, createToken),
            in_jsonResponse=False
        )
        verify_HTTP_status_code(delete_response, 201)
        verify_delete_response(delete_response.text)
        put_url=delete_url
        put_response=put_request(
            URl=put_url,
            Auth=None,
            in_jsonResponse=False,
            pay_load=payload_update_booking(),
            Headers=utils.common_header_put_patch_delete_basic_cookie(self, createToken),
        )
        verify_HTTP_status_code(put_response,405)









