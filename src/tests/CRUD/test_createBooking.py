

import allure
import pytest
import logging # This is used to print the messages; Inbuilt in python

from src.Helpers.api_requests_wrapper import  post_request
from src.Helpers.payload_manager import payload_create_booking
from src.Helpers.common_verification import *
from src.Constants.api_constants import APIConstants
from src.utils.utils import  *

class TestCreateBooking(object):
    @allure.title("Verify that create booking status and Booking id shouldnot be  null")
    @allure.description("create a Booking from the payload and verify that booking id should not be null")
    @pytest.mark.positive
    def test_create_booking_positive(self):
        #URl,Auth,pay_load,Headers,in_jsonResponse
        Logger=logging.getLogger(__name__)
        Logger.info("Post req Started")
        response=post_request(
            URl=APIConstants().url_create_booking(),
            Auth=None,
            pay_load=payload_create_booking(),
            Headers=utils().common_headers_json(),
            in_jsonResponse=False

        )
        Logger.info("Post req Done")
        Logger.info ("Now verify")
        verify_HTTP_status_code(response_data=response,expected_data=200)
        Logger.info("Response i got")
        verify_json_key_not_null(response.json()["bookingid"])
        verify_json_key_gr_zero(response.json()["bookingid"])


    @allure.title("Verify that create booking with empty payload")
    @allure.description("create a Booking id invalid, verify 500 for the empty payload")
    @pytest.mark.negative
    def test_create_booking_negative_tc1(self):
        Logger = logging.getLogger(__name__)
        response=post_request(
            # URl,Auth,pay_load,Headers,in_jsonResponse
            URl=APIConstants().url_create_booking(),
            Auth=None,
            pay_load={},
            Headers=utils().common_headers_json(),
            in_jsonResponse=False

        )
        Logger.info("Post req negative Done")
        Logger.info("Now verify")
        verify_HTTP_status_code(response_data=response,expected_data=500)

    @allure.title("Verify that create booking with incorrect Json")
    @allure.description("create a Booking id invalid, verify 500 for the incorrect Json")
    @pytest.mark.negative
    def test_create_booking_negative_tc2(self):
        Logger = logging.getLogger(__name__)
        response = post_request(
            # URl,Auth,pay_load,Headers,in_jsonResponse
            URl=APIConstants().url_create_booking(),
            Auth=None,
            pay_load={"name": "Andrea"},
            Headers=utils().common_headers_json(),
            in_jsonResponse=False

        )
        Logger.info("Post req negative Done")
        Logger.info("Now verify")
        verify_HTTP_status_code(response_data=response, expected_data=500)

    @allure.title("Verify that create booking with incomplete json")
    @allure.description("create a Booking id invalid, verify 500 for the incomplete json")
    @pytest.mark.negative
    def test_create_booking_negative_tc3(self):
        Logger = logging.getLogger(__name__)
        response = post_request(
            # URl,Auth,pay_load,Headers,in_jsonResponse
            URl=APIConstants().url_create_booking(),
            Auth=None,
            pay_load={"name": None},
            Headers=utils().common_headers_json(),
            in_jsonResponse=False

        )
        Logger.info("Post req negative Done")
        Logger.info("Now verify")
        verify_HTTP_status_code(response_data=response, expected_data=500)









