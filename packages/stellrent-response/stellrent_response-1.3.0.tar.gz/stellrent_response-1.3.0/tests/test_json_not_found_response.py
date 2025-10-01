from stellrent_response import json_response
from flask import Response
import json

detailed_error_message = "A detailed error message"
custom_message = "A custom Bad Request message"
default_message = "Bad Request"
default_content_type = "application/json"

def test_response_not_found():
    not_found_response = json_response.NotFound(message=custom_message, details=detailed_error_message)
    not_found_response.response_message = custom_message
    assert(not_found_response.status_code == 404)
    assert(not_found_response.data == None)
    assert(not_found_response.message == custom_message)
    assert(not_found_response.details == detailed_error_message)
    response_obj = not_found_response.make_response()
    assert(isinstance(response_obj, Response))
    assert(response_obj.status_code == 404)
    assert(response_obj.content_type == default_content_type)
    assert(not_found_response.details == detailed_error_message)
    response_data_dict = json.loads(response_obj.get_data())
    assert(len(response_data_dict) == 3)
    assert(response_data_dict['message'] == custom_message)
    assert(response_data_dict['details'] == detailed_error_message)
    assert(response_data_dict['status'] == 404)
