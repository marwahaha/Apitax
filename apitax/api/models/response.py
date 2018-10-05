# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apitax.api.models.base_model_ import Model
from apitax.api import util


class Response(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, status=None, message=None, body=None, log=None):  # noqa: E501
        """Response - a model defined in Swagger

        :param status: The status of this Response.  # noqa: E501
        :type status: int
        :param message: The message of this Response.  # noqa: E501
        :type message: str
        :param body: The body of this Response.  # noqa: E501
        :type body: object
        :param log: The log of this Response.  # noqa: E501
        :type log: str
        """
        self.swagger_types = {
            'status': int,
            'message': str,
            'body': object,
            'log': str
        }

        self.attribute_map = {
            'status': 'status',
            'message': 'message',
            'body': 'body',
            'log': 'log'
        }

        self._status = status
        self._message = message
        self._body = body
        self._log = log

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Response of this Response.  # noqa: E501
        :rtype: Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this Response.


        :return: The status of this Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Response.


        :param status: The status of this Response.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this Response.


        :return: The message of this Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Response.


        :param message: The message of this Response.
        :type message: str
        """

        self._message = message

    @property
    def body(self):
        """Gets the body of this Response.


        :return: The body of this Response.
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Response.


        :param body: The body of this Response.
        :type body: object
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def log(self):
        """Gets the log of this Response.


        :return: The log of this Response.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Response.


        :param log: The log of this Response.
        :type log: str
        """

        self._log = log
