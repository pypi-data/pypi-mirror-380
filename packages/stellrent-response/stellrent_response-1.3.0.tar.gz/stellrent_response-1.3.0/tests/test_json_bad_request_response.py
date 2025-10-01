from stellrent_response import json_response
from flask import Response
import json
from pydantic import BaseModel, Field, ValidationError

detailed_error_message = "A detailed error message"
custom_message = "A custom Bad Request message"
default_message = "Bad Request"
import pytest
default_content_type = "application/json"

class TestSchema(BaseModel):
    name: str = Field(...)
    id: int = Field(...)
    cellphone: str = Field(...)

def __test_basic_bad_response(response:json_response.BadRequest):
    assert(response.status_code == 400)
    assert(response.data == None)
    assert(response.message is not None)
    response_obj = response.make_response()
    assert(response_obj.status_code == 400)
    assert(response_obj.content_type == default_content_type)
    assert(isinstance(response_obj, Response))

def test_response():
    bad_request_response = json_response.BadRequest(message=None, details=None)
    __test_basic_bad_response(bad_request_response)
    assert(bad_request_response.details == None)
    bad_request_response_obj = bad_request_response.make_response()
    response_data_dict = json.loads(bad_request_response_obj.get_data())
    assert(len(response_data_dict) == 2)
    assert(response_data_dict['message'] == json_response.default_messages[400])
    assert(response_data_dict['status'] == 400)

def test_response_with_details():
    bad_request_response = json_response.BadRequest(details=detailed_error_message)
    __test_basic_bad_response(bad_request_response)
    assert(bad_request_response.details is not None)
    response_obj = bad_request_response.make_response()
    response_data_dict = json.loads(response_obj.get_data())
    assert(len(response_data_dict) == 3)
    assert(response_data_dict['details'] == detailed_error_message)
    assert(response_data_dict['message'] == json_response.default_messages[400])
    assert(response_data_dict['status'] == 400)

def test_response_with_custom_message():
    bad_request_response = json_response.BadRequest(message=custom_message)
    __test_basic_bad_response(bad_request_response)
    assert(bad_request_response.details is None)
    response_obj = bad_request_response.make_response()
    response_data_dict = json.loads(response_obj.get_data())
    assert(len(response_data_dict) == 2)
    assert(response_data_dict['message'] == custom_message)
    assert(response_data_dict['status'] == 400)

def test_response_with_details_and_custom_message():
    bad_request_response = json_response.BadRequest(message=custom_message, details=detailed_error_message)
    __test_basic_bad_response(bad_request_response)
    assert(bad_request_response.details is not None)
    response_obj = bad_request_response.make_response()
    response_data_dict = json.loads(response_obj.get_data())
    assert(len(response_data_dict) == 3)
    assert(response_data_dict['message'] == custom_message)
    assert(response_data_dict['details'] == detailed_error_message)
    assert(response_data_dict['status'] == 400)

def test_response_with_pydantic_validation_error():
    """
    Testa a geração de uma resposta BadRequest a partir de um Pydantic ValidationError.
    Usa pytest.raises para capturar a exceção de forma idiomática.
    """
    with pytest.raises(ValidationError) as excinfo:
        TestSchema(name="Adamastor", id="not int", cellphone=None)

    # A exceção foi capturada, agora podemos usá-la para criar nossa resposta
    e = excinfo.value
    bad_request_response = json_response.BadRequest(validate_exception=e)

    __test_basic_bad_response(bad_request_response)
    assert bad_request_response.details is not None
    assert isinstance(bad_request_response.details, list)
    assert len(bad_request_response.details) == 2 # Esperamos erros para 'id' e 'cellphone'

    response_obj = bad_request_response.make_response()
    response_data_dict = json.loads(response_obj.get_data())

    assert response_data_dict['details'][0]['loc'] == ['id']
    assert response_data_dict['details'][0]['msg'] == 'Input should be a valid integer, unable to parse string as an integer'
    assert response_data_dict['details'][1]['loc'] == ['cellphone']
    assert response_data_dict['details'][1]['msg'] == 'Input should be a valid string'
    # bad_request_object = json_response.BadRequest(validate_exception=e)
    # assert(bad_request_object.details is not None)
        # response_obj = bad_request_response.make_response()
        # response_data_dict = json.loads(response_obj.get_data())
        # assert(len(response_data_dict) == 3)
        # assert(response_data_dict['message'] == custom_message)
        # assert(response_data_dict['details'] == detailed_error_message)
        # assert(response_data_dict['status'] == 400)
