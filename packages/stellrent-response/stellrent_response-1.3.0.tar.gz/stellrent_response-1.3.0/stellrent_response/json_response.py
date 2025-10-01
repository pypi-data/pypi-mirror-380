# -*- coding: utf-8 -*-
import logging
import json
import uuid # Importa o módulo uuid
import datetime # Importa o módulo datetime para o encoder
from flask import Response
from typing import Any, Dict, List, Optional, Union

# Dicionário de mensagens padrão para códigos de status HTTP
default_messages = {
    200: "Request executed successfully",
    201: "Created",
    204: None,  # No Content has no message body
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Resource Not Found",
    405: "Method not allowed",
    500: "Internal Server Error"
}

class CustomJsonEncoder(json.JSONEncoder):
    """
    Um encoder JSON personalizado que sabe como serializar objetos UUID e datetime.
    """
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj) # Converte objetos UUID para sua representação em string
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat() # Converte objetos datetime para o formato ISO 8601
        return json.JSONEncoder.default(self, obj) # Delega para o encoder padrão para outros tipos

class ApiResponse: # Renomeado de DefaultResponse para clareza
    """
    Classe base para padronizar as respostas da API Flask.
    Define a estrutura comum para respostas de sucesso e erro.
    """
    _logger: logging.Logger
    _status_code: int
    _message: Optional[str]
    _data: Optional[Any] # Representa o 'response_data' original
    _details: Optional[Any] # Representa o 'response_details' original
    _errors: Optional[List[Dict]] # Adicionado para erros de validação, se usado

    def __init__(
        self,
        status_code: int,
        message: Optional[str] = None, # Corresponde ao 'response_message'
        data: Optional[Any] = None, # Corresponde ao 'response_data'
        details: Optional[Any] = None, # Corresponde ao 'response_details'
        errors: Optional[List[Dict]] = None, # Novo, para erros de validação
        logger: Optional[logging.Logger] = None
    ):
        """
        Inicializa uma nova instância de ApiResponse.

        Args:
            status_code (int): O código de status HTTP da resposta.
            message (Optional[str]): Uma mensagem amigável para o usuário.
                                     Se None, será usado o default_messages.
            data (Optional[Any]): Os dados reais da resposta de sucesso.
                                  Se fornecido, será o corpo JSON completo.
            details (Optional[Any]): Detalhes adicionais sobre a resposta.
            errors (Optional[List[Dict]]): Lista de erros específicos (útil para erros de validação).
            logger (Optional[logging.Logger]): Uma instância de logger para uso interno.
        """
        if logger and isinstance(logger, logging.Logger):
            self._logger = logger
        else:
            self._logger = logging.getLogger(self.__class__.__name__)
            if logger is not None: # A logger was provided but was invalid
                self._logger.warning(
                    f"Invalid logger type: {type(logger)}. Expected {logging.Logger}. "
                    f"Using default logger '{self._logger.name}'."
                )
        
        self._status_code = status_code
        self._message = message if message is not None else default_messages.get(status_code)
        self._data = data
        self._details = details
        self._errors = errors # Armazena os erros para serem incluídos, se aplicável

    def make_response(self) -> Response:
        """
        Cria e retorna um objeto Flask Response padronizado, respeitando
        o contrato de API original.

        Returns:
            Response: O objeto de resposta do Flask.
        """
        if self._status_code == 204:
            # HTTP 204 No Content responses must not include a message-body
            # or a Content-Type header.
            return Response(status=204, mimetype="")

        # --- Lógica para Respeitar o Contrato Original ---
        # Se 'data' foi fornecido, ele se torna o corpo JSON completo.
        if self._data is not None:
            json_response_payload = json.dumps(self._data, cls=CustomJsonEncoder)
            response = Response(
                content_type="application/json",
                status=self._status_code,
                response=json_response_payload
            )
            return response
        
        # Caso 'data' seja None, constrói o corpo da resposta com 'message', 'details' e 'status'.
        response_body: Dict[str, Any] = {}
        
        if self._message is not None:
            response_body["message"] = self._message
        if self._details is not None:
            response_body["details"] = self._details

        # Adiciona a lista de erros para Bad Requests ou outros erros de validação
        if self._errors is not None and self._status_code >= 400: # Normalmente para erros
            response_body["errors"] = self._errors
        
        # Adiciona 'status' numérico apenas se houver outros campos no corpo,
        # conforme a lógica original do seu código.
        if response_body:
            response_body["status"] = self._status_code
        # Fallback para erros quando o corpo está vazio (apenas status e mensagem padrão)
        elif self._status_code >= 400:
            fallback_message = default_messages.get(self._status_code, "Error")
            response_body = {"message": fallback_message, "status": self._status_code}
            
        json_response_payload = json.dumps(response_body, cls=CustomJsonEncoder)

        response = Response(
            content_type="application/json",
            status=self._status_code,
            response=json_response_payload
        )
        return response
    
    # Propriedades de leitura para os atributos internos (boa prática)
    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def message(self) -> Optional[str]:
        return self._message

    @property
    def data(self) -> Optional[Any]:
        return self._data

    @property
    def details(self) -> Optional[Any]:
        return self._details

    @property
    def errors(self) -> Optional[List[Dict]]:
        return self._errors

# --- Classes para Respostas de Sucesso ---

class DataResponse(ApiResponse):
    """
    Resposta de sucesso que contém dados.
    Corresponde a um status HTTP 200 OK por padrão.
    O corpo da resposta será APENAS os dados fornecidos.
    """
    def __init__(
        self, 
        data: Any, # Deve ser fornecido para esta classe
        status_code: int = 200,
        logger: Optional[logging.Logger] = None
    ):
        # Para DataResponse, a mensagem e detalhes não são parte do corpo JSON,
        # mas a classe base precisa deles para inicialização.
        # Eles não serão incluídos no JSON final devido à lógica de make_response.
        super().__init__(
            status_code=status_code,
            message=None, # Define a mensagem padrão
            data=data,
            details=None, # Não usado neste tipo de resposta para o corpo JSON
            errors=None,
            logger=logger
        )

class ConfirmationResponse(ApiResponse):
    """
    Resposta de sucesso sem dados específicos, para confirmações gerais.
    Corresponde a um status HTTP 200 OK por padrão.
    O corpo da resposta será um envelope com message, details e status.
    """
    def __init__(
        self, 
        message: Optional[str] = None, # Permite customizar a mensagem
        details: Optional[Any] = None, 
        status_code: int = 200,
        logger: Optional[logging.Logger] = None
    ):
        super().__init__(
            status_code=status_code,
            message=message if message is not None else default_messages[status_code],
            data=None, # Garante que o corpo estruturado seja usado
            details=details,
            errors=None,
            logger=logger
        )

class CreateConfirmationResponse(ApiResponse):
    """
    Resposta de sucesso para criação de recursos.
    Corresponde a um status HTTP 201 Created por padrão.
    O corpo da resposta será um envelope com message, details e status.
    Se 'data' for fornecido, a lógica da classe base fará com que seja o corpo JSON direto.
    """
    def __init__(
        self, 
        data: Optional[Any] = None, # Pode ser o recurso criado, ou None para um envelope simples
        message: Optional[str] = None, 
        details: Optional[Any] = None, 
        logger: Optional[logging.Logger] = None
    ):
        super().__init__(
            status_code=201,
            message=message if message is not None else default_messages[201],
            data=data, # Este é o 'response_data' que make_response vai verificar
            details=details,
            errors=None,
            logger=logger
        )
        
class NoDataResponse(ApiResponse):
    """
    Resposta para requisições que resultam em "No Content".
    Corresponde a um status HTTP 204 No Content. O corpo da resposta será vazio.
    """
    def __init__(self, logger: Optional[logging.Logger] = None):
        super().__init__(
            status_code=204,
            message=None, # 204 não deve ter mensagem no corpo
            data=None,
            details=None,
            errors=None,
            logger=logger
        )

# --- Classes para Respostas de Erro ---

class ErrorResponse(ApiResponse):
    """
    Classe base para respostas de erro.
    Define a estrutura comum para mensagens de erro, incluindo o status numérico.
    """
    def __init__(
        self, 
        status_code: int, 
        message: Optional[str] = None, 
        details: Optional[Any] = None, 
        errors: Optional[List[Dict]] = None, # Para erros de validação
        logger: Optional[logging.Logger] = None
    ):
        # Para erros, garantimos que 'data' seja None para usar o corpo estruturado.
        super().__init__(
            status_code=status_code,
            message=message if message is not None else default_messages.get(status_code),
            data=None, # Erros não devem ter 'data' diretamente no corpo
            details=details,
            errors=errors,
            logger=logger
        )


class BadRequest(ErrorResponse):
    from pydantic import ValidationError
    """
    Erro 400 Bad Request: A requisição não pôde ser entendida ou processada.
    """
    def __init__(
        self, 
        message: Optional[str] = None, # Permite customizar a mensagem
        details: Optional[Any] = None, 
        errors: Optional[List[Dict]] = None, # Para erros de validação de campos
        logger: Optional[logging.Logger] = None,
        validate_exception: Optional[ValidationError] = None, # Permite customizar details com base em um ValidationError(Pydantic)
    ):
        if validate_exception is not None:
           details = self.parser_pydantic_validation_error(validate_exception)
        super().__init__(
            status_code=400,
            message=message,
            details=details,
            errors=errors,
            logger=logger
        )
    def parser_pydantic_validation_error(self, validate_exception: ValidationError) -> List[Dict[str, Any]]:
        """
        Converte um Pydantic ValidationError em uma lista de dicionários com detalhes do erro.
        """
        return validate_exception.errors()
        

class Unauthorized(ErrorResponse):
    """
    Erro 401 Unauthorized: A autenticação é necessária e falhou ou não foi fornecida.
    """
    def __init__(
        self, 
        message: Optional[str] = None, 
        details: Optional[Any] = None, 
        logger: Optional[logging.Logger] = None
    ):
        super().__init__(
            status_code=401,
            message=message, 
            details=details,
            logger=logger
        )

class Forbidden(ErrorResponse):
    """
    Erro 403 Forbidden: O servidor entendeu a requisição, mas se recusa a autorizá-la.
    """
    def __init__(
        self, 
        message: Optional[str] = None, 
        details: Optional[Any] = None, 
        logger: Optional[logging.Logger] = None
    ):
        super().__init__(
            status_code=403,
            message=message,
            details=details,
            logger=logger
        )

class NotFound(ErrorResponse):
    """
    Erro 404 Not Found: O recurso solicitado não pôde ser encontrado.
    """
    def __init__(
        self, 
        message: Optional[str] = None, 
        details: Optional[Any] = None, 
        logger: Optional[logging.Logger] = None
    ):
        super().__init__(
            status_code=404,
            message=message,
            details=details,
            logger=logger
        )

class MethodNotAllowed(ErrorResponse):
    """
    Erro 405 Method Not Allowed: O método HTTP da requisição não é permitido para o recurso.
    """
    def __init__(
        self, 
        message: Optional[str] = None, 
        details: Optional[Any] = None, 
        logger: Optional[logging.Logger] = None
    ):
        super().__init__(
            status_code=405,
            message=message,
            details=details,
            logger=logger
        )

class ServerError(ErrorResponse):
    """
    Erro 500 Internal Server Error: Um erro inesperado ocorreu no servidor.
    """
    def __init__(
        self, 
        message: Optional[str] = None, 
        details: Optional[Any] = None, 
        logger: Optional[logging.Logger] = None
    ):
        super().__init__(
            status_code=500,
            message=message,
            details=details,
            logger=logger
        )
