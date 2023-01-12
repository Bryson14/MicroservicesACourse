# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Item(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, price=None):  # noqa: E501
        """Item - a model defined in OpenAPI

        :param id: The id of this Item.  # noqa: E501
        :type id: int
        :param name: The name of this Item.  # noqa: E501
        :type name: str
        :param price: The price of this Item.  # noqa: E501
        :type price: float
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'price': float
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'Name',
            'price': 'Price'
        }

        self._id = id
        self._name = name
        self._price = price

    @classmethod
    def from_dict(cls, dikt) -> 'Item':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Item of this Item.  # noqa: E501
        :rtype: Item
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Item.


        :return: The id of this Item.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Item.


        :param id: The id of this Item.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Item.


        :return: The name of this Item.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Item.


        :param name: The name of this Item.
        :type name: str
        """

        self._name = name

    @property
    def price(self):
        """Gets the price of this Item.


        :return: The price of this Item.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Item.


        :param price: The price of this Item.
        :type price: float
        """

        self._price = price