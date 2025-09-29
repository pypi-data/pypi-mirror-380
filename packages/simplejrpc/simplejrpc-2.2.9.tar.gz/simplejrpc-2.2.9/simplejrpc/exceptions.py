# -*- encoding: utf-8 -*-
import http
import json
from typing import Any

from simplejrpc._json import _jsonify  # type: ignore


class RPCException(Exception):
    """基础RPC异常"""

    def __init__(
        self,
        message: Any = http.HTTPStatus.BAD_REQUEST.description,
        code: Any = http.HTTPStatus.BAD_REQUEST.value,
        data: Any = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.message = message
        self.code = code
        self.data = data

    def __str__(self):
        """ """
        from simplejrpc._text import TextMessageDecoder  # type: ignore

        data = _jsonify(code=self.code, data=self.data, msg=self.message)
        return json.dumps(data, cls=TextMessageDecoder)


class UnauthorizedError(RPCException):
    """未授权异常"""


class ValidationError(RPCException):
    """验证异常"""


class RuntimeError(RPCException):
    """ """


class FileNotFoundError(RPCException):
    """ """


class ValueError(RPCException):
    """ """


class AttributeError(RPCException):
    """ """


class TypeError(RPCException):
    """ """
