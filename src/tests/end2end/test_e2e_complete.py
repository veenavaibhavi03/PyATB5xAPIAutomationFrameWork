import allure
import pytest
from requests import Response

from src.Constants.api_constants import APIConstants
from src.Helpers.api_requests_wrapper import put_request, delete_request
from src.Helpers.common_verification import verify_response_key, verify_HTTP_status_code, verify_json_key_gr_zero, \
    verify_delete_response
from src.Helpers.payload_manager import payload_update_booking
from src.utils.utils import utils


class TestE2E(object):
    @pytest.mark.positive
    @allure.title("E2E-createBooking->Update-> Delete")
    @allure.description("verify that created booking id when we update we are able to update it and delete it also --Full CRUD")
    def test_update_booking_with_id_token(self, createToken, get_booking_id):
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
            pay_load=payload_update_booking(),
            in_jsonResponse=False

        )
        # print(Put_response.json()["firstname"])
        verify_response_key(Put_response.json()["firstname"], "Marina")
        verify_response_key(Put_response.json()["lastname"], "Anthony")
        verify_HTTP_status_code(Put_response, 200)

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description(
        "verify that created booking id gets deleted")
    @pytest.mark.positive
    def test_delete_booking_with_id_token(self,createToken, get_booking_id):
        print(createToken, get_booking_id)
        delete_url = APIConstants.url_patch_put_delete(booking_id=get_booking_id)
        print(delete_url)
        # URl,Auth,pay_load,Headers,in_jsonResponse
        delete_response = delete_request(
            URl=delete_url,
            Auth=None,
            Headers=utils.common_header_put_patch_delete_basic_cookie(self,createToken),
            in_jsonResponse=False
        )
        verify_HTTP_status_code(delete_response,201)
        verify_delete_response(delete_response.text)

























