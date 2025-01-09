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

class Test_E2E(object):
    @pytest.mark.positive
    @allure.title("E2E-createBooking->Update-> Delete")
    @allure.description("verify that created booking id when we update we are able to update it and delete it also --Full CRUD")
    def test_update_bookingid_without_token(self,get_booking_id):
        #print(createToken,get_booking_id)
        BookingId=get_booking_id
        put_url=APIConstants.url_patch_put_delete(booking_id=BookingId)
        #print(put_url)
        Put_response=put_request(
            #(URl: Any,Auth: Any,pay_load: Any,Headers: Any,in_jsonResponse: {__eq__}) -> Response
            URl=put_url,
            Headers=None,
            Auth=None,
            pay_load=payload_update_booking(),
            in_jsonResponse=False

        )
        #print(Put_response.json()["firstname"])
        #verify_response_key(Put_response.json()["firstname"], "Mark")
        #verify_response_key(Put_response.json()["lastname"], "Anthony")
        verify_HTTP_status_code(Put_response,403)

