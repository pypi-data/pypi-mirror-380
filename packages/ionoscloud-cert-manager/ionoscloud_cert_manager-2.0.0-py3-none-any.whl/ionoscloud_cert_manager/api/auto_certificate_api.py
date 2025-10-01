from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_cert_manager.api_client import ApiClient
from ionoscloud_cert_manager.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AutoCertificateApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def auto_certificates_delete(self, auto_certificate_id, **kwargs):  # noqa: E501
        """Delete AutoCertificate  # noqa: E501

        Deletes the specified AutoCertificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_delete(auto_certificate_id, async_req=True)
        >>> result = thread.get()

        :param auto_certificate_id: The ID (UUID) of the AutoCertificate. (required)
        :type auto_certificate_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.auto_certificates_delete_with_http_info(auto_certificate_id, **kwargs)  # noqa: E501

    def auto_certificates_delete_with_http_info(self, auto_certificate_id, **kwargs):  # noqa: E501
        """Delete AutoCertificate  # noqa: E501

        Deletes the specified AutoCertificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_delete_with_http_info(auto_certificate_id, async_req=True)
        >>> result = thread.get()

        :param auto_certificate_id: The ID (UUID) of the AutoCertificate. (required)
        :type auto_certificate_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'auto_certificate_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auto_certificates_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'auto_certificate_id' is set
        if self.api_client.client_side_validation and ('auto_certificate_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['auto_certificate_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `auto_certificate_id` when calling `auto_certificates_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auto_certificate_id' in local_var_params:
            path_params['autoCertificateId'] = local_var_params['auto_certificate_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/auto-certificates/{autoCertificateId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def auto_certificates_find_by_id(self, auto_certificate_id, **kwargs):  # noqa: E501
        """Retrieve AutoCertificate  # noqa: E501

        Returns the AutoCertificate by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_find_by_id(auto_certificate_id, async_req=True)
        >>> result = thread.get()

        :param auto_certificate_id: The ID (UUID) of the AutoCertificate. (required)
        :type auto_certificate_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AutoCertificateRead
        """
        kwargs['_return_http_data_only'] = True
        return self.auto_certificates_find_by_id_with_http_info(auto_certificate_id, **kwargs)  # noqa: E501

    def auto_certificates_find_by_id_with_http_info(self, auto_certificate_id, **kwargs):  # noqa: E501
        """Retrieve AutoCertificate  # noqa: E501

        Returns the AutoCertificate by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_find_by_id_with_http_info(auto_certificate_id, async_req=True)
        >>> result = thread.get()

        :param auto_certificate_id: The ID (UUID) of the AutoCertificate. (required)
        :type auto_certificate_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AutoCertificateRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'auto_certificate_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auto_certificates_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'auto_certificate_id' is set
        if self.api_client.client_side_validation and ('auto_certificate_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['auto_certificate_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `auto_certificate_id` when calling `auto_certificates_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auto_certificate_id' in local_var_params:
            path_params['autoCertificateId'] = local_var_params['auto_certificate_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'AutoCertificateRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/auto-certificates/{autoCertificateId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def auto_certificates_get(self, **kwargs):  # noqa: E501
        """Retrieve all AutoCertificate  # noqa: E501

        This endpoint enables retrieving all AutoCertificate using pagination and optional filters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_get(async_req=True)
        >>> result = thread.get()

        :param offset: The first element (of the total list of elements) to include in the response. Use together with limit for pagination.
        :type offset: int
        :param limit: The maximum number of elements to return. Use together with offset for pagination.
        :type limit: int
        :param filter_common_name: Filter by the common name (DNS). 
        :type filter_common_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AutoCertificateReadList
        """
        kwargs['_return_http_data_only'] = True
        return self.auto_certificates_get_with_http_info(**kwargs)  # noqa: E501

    def auto_certificates_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all AutoCertificate  # noqa: E501

        This endpoint enables retrieving all AutoCertificate using pagination and optional filters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param offset: The first element (of the total list of elements) to include in the response. Use together with limit for pagination.
        :type offset: int
        :param limit: The maximum number of elements to return. Use together with offset for pagination.
        :type limit: int
        :param filter_common_name: Filter by the common name (DNS). 
        :type filter_common_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AutoCertificateReadList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'limit',
            'filter_common_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auto_certificates_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `auto_certificates_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `auto_certificates_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `auto_certificates_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'filter_common_name' in local_var_params and local_var_params['filter_common_name'] is not None:  # noqa: E501
            query_params.append(('filter.commonName', local_var_params['filter_common_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'AutoCertificateReadList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/auto-certificates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def auto_certificates_patch(self, auto_certificate_id, auto_certificate_patch, **kwargs):  # noqa: E501
        """Updates AutoCertificate  # noqa: E501

        Changes AutoCertificate with the provided ID. Values provides will replace the existing data.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_patch(auto_certificate_id, auto_certificate_patch, async_req=True)
        >>> result = thread.get()

        :param auto_certificate_id: The ID (UUID) of the AutoCertificate. (required)
        :type auto_certificate_id: str
        :param auto_certificate_patch: patch AutoCertificate (required)
        :type auto_certificate_patch: AutoCertificatePatch
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AutoCertificateRead
        """
        kwargs['_return_http_data_only'] = True
        return self.auto_certificates_patch_with_http_info(auto_certificate_id, auto_certificate_patch, **kwargs)  # noqa: E501

    def auto_certificates_patch_with_http_info(self, auto_certificate_id, auto_certificate_patch, **kwargs):  # noqa: E501
        """Updates AutoCertificate  # noqa: E501

        Changes AutoCertificate with the provided ID. Values provides will replace the existing data.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_patch_with_http_info(auto_certificate_id, auto_certificate_patch, async_req=True)
        >>> result = thread.get()

        :param auto_certificate_id: The ID (UUID) of the AutoCertificate. (required)
        :type auto_certificate_id: str
        :param auto_certificate_patch: patch AutoCertificate (required)
        :type auto_certificate_patch: AutoCertificatePatch
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AutoCertificateRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'auto_certificate_id',
            'auto_certificate_patch'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auto_certificates_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'auto_certificate_id' is set
        if self.api_client.client_side_validation and ('auto_certificate_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['auto_certificate_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `auto_certificate_id` when calling `auto_certificates_patch`")  # noqa: E501
        # verify the required parameter 'auto_certificate_patch' is set
        if self.api_client.client_side_validation and ('auto_certificate_patch' not in local_var_params or  # noqa: E501
                                                        local_var_params['auto_certificate_patch'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `auto_certificate_patch` when calling `auto_certificates_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auto_certificate_id' in local_var_params:
            path_params['autoCertificateId'] = local_var_params['auto_certificate_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'auto_certificate_patch' in local_var_params:
            body_params = local_var_params['auto_certificate_patch']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'AutoCertificateRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/auto-certificates/{autoCertificateId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def auto_certificates_post(self, auto_certificate_create, **kwargs):  # noqa: E501
        """Create AutoCertificate  # noqa: E501

        Creates a new AutoCertificate.  The full AutoCertificate needs to be provided to create the object. Optional data will be filled with defaults or left empty.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_post(auto_certificate_create, async_req=True)
        >>> result = thread.get()

        :param auto_certificate_create: AutoCertificate to create. (required)
        :type auto_certificate_create: AutoCertificateCreate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AutoCertificateRead
        """
        kwargs['_return_http_data_only'] = True
        return self.auto_certificates_post_with_http_info(auto_certificate_create, **kwargs)  # noqa: E501

    def auto_certificates_post_with_http_info(self, auto_certificate_create, **kwargs):  # noqa: E501
        """Create AutoCertificate  # noqa: E501

        Creates a new AutoCertificate.  The full AutoCertificate needs to be provided to create the object. Optional data will be filled with defaults or left empty.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auto_certificates_post_with_http_info(auto_certificate_create, async_req=True)
        >>> result = thread.get()

        :param auto_certificate_create: AutoCertificate to create. (required)
        :type auto_certificate_create: AutoCertificateCreate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AutoCertificateRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'auto_certificate_create'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auto_certificates_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'auto_certificate_create' is set
        if self.api_client.client_side_validation and ('auto_certificate_create' not in local_var_params or  # noqa: E501
                                                        local_var_params['auto_certificate_create'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `auto_certificate_create` when calling `auto_certificates_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'auto_certificate_create' in local_var_params:
            body_params = local_var_params['auto_certificate_create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'AutoCertificateRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/auto-certificates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
