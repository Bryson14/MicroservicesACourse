# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.order import Order  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_delete_order(self):
        """Test case for delete_order

        Cancels an order
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/order/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_id_get(self):
        """Test case for order_id_get

        Returns a given order id as json
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/order/{id}'.format(id=10),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_post(self):
        """Test case for order_post

        Add a new order
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/order',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_get(self):
        """Test case for orders_get

        Returns a list of all orders
        """
        query_string = [('customerName', 'customer_name_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/orders',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_path_order(self):
        """Test case for path_order

        Update an existing order
        """
        order = {"createdTimestamp":"2000-01-23T04:56:07.000+00:00","discount":2.0,"id":10,"orderItems":[{"Price":6.0274563,"id":0,"Name":"Best Latte Ever"},{"Price":6.0274563,"id":0,"Name":"Best Latte Ever"}],"customerName":"Huzaifah Shamim","status":"placed"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1/order/{id}'.format(id=10),
            method='PATCH',
            headers=headers,
            data=json.dumps(order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
