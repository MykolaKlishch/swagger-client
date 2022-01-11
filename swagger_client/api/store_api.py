# coding: utf-8

"""
    Swagger Petstore

    <this is not the same file> This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class StoreApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_order(self, order_id, **kwargs):  # noqa: E501
        """Delete purchase order by ID  # noqa: E501

        For valid response try integer IDs with positive integer value.         Negative or non-integer values will generate API errors  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_order(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int order_id: ID of the order that needs to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_order_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_order_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def delete_order_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """Delete purchase order by ID  # noqa: E501

        For valid response try integer IDs with positive integer value.         Negative or non-integer values will generate API errors  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_order_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int order_id: ID of the order that needs to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if self.api_client.client_side_validation and ('order_id' not in params or
                                                       params['order_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `order_id` when calling `delete_order`")  # noqa: E501

        if self.api_client.client_side_validation and ('order_id' in params and params['order_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `order_id` when calling `delete_order`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/store/order/{orderId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_inventory(self, **kwargs):  # noqa: E501
        """Returns pet inventories by status  # noqa: E501

        Returns a map of status codes to quantities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inventory(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_inventory_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_inventory_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_inventory_with_http_info(self, **kwargs):  # noqa: E501
        """Returns pet inventories by status  # noqa: E501

        Returns a map of status codes to quantities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inventory_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/store/inventory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, int)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_order_by_id(self, order_id, **kwargs):  # noqa: E501
        """Find purchase order by ID  # noqa: E501

        For valid response try integer IDs with value >= 1 and <= 10.         Other values will generated exceptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_by_id(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int order_id: ID of pet that needs to be fetched (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_by_id_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_by_id_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def get_order_by_id_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """Find purchase order by ID  # noqa: E501

        For valid response try integer IDs with value >= 1 and <= 10.         Other values will generated exceptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_by_id_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int order_id: ID of pet that needs to be fetched (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if self.api_client.client_side_validation and ('order_id' not in params or
                                                       params['order_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `order_id` when calling `get_order_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and ('order_id' in params and params['order_id'] > 10):  # noqa: E501
            raise ValueError("Invalid value for parameter `order_id` when calling `get_order_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and ('order_id' in params and params['order_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `order_id` when calling `get_order_by_id`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/store/order/{orderId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Order',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def place_order(self, body, **kwargs):  # noqa: E501
        """Place an order for a pet  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Order body: order placed for purchasing the pet (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.place_order_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.place_order_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def place_order_with_http_info(self, body, **kwargs):  # noqa: E501
        """Place an order for a pet  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Order body: order placed for purchasing the pet (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `place_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/store/order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Order',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
