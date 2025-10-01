from stellrent_response import json_response
from flask import Response

default_content_type = "application/json"

def test_nocontent_response():
    no_content_response = json_response.NoDataResponse()
    assert(no_content_response.status_code == 204)
    assert(no_content_response.data == None)
    assert(no_content_response.message == None)
    assert(no_content_response.details == None)
    response_obj = no_content_response.make_response()
    assert(response_obj.content_length is None)
    assert(response_obj.status_code == 204)
    assert(hasattr(response_obj, 'content_type') == True)
    assert(response_obj.content_type == "")
    assert(isinstance(response_obj, Response))
