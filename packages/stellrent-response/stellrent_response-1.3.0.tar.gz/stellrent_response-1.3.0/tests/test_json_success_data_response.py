from stellrent_response import json_response
from flask import Response
from pydantic import validate_call
import json

default_content_type = "application/json"

content_response_data = {
    "param1": "value1",
    "param2": "value2",
    "param3": "value3",
    "param4": "value4"
 }

def test_response():
    success_content_resp = json_response.DataResponse(data=content_response_data)
    # Primeiro validamos os atributos da classe gerada, sem os filtros de geração do Flask Response
    assert(success_content_resp.status_code == 200)
    assert(success_content_resp.data == content_response_data)
    assert(success_content_resp.message == json_response.default_messages[200])
    assert(success_content_resp.details == None)
    response_obj = success_content_resp.make_response()
    # Primeiro validamos os atributos da Flask Response gerada
    assert(response_obj.content_length is not None)
    assert(response_obj.content_length > 0)
    assert(response_obj.status_code == 200)
    assert(response_obj.content_type == default_content_type)
    assert(isinstance(response_obj, Response))
    # Validação do conteudo gerado no Response Body
    response_data_dict = json.loads(response_obj.get_data())
    assert(len(content_response_data) == len(response_data_dict))
    assert(content_response_data == response_data_dict)