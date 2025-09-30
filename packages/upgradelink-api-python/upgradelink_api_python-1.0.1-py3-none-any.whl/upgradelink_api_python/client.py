# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.request import TeaRequest
from Tea.exceptions import TeaException, UnretryableException
from Tea.core import TeaCore

from upgradelink_api_python import models as upgrade_link_models
from alibabacloud_tea_util.client import Client as UtilClient
from darabonba_base_python.client import Client as DarabonbaBaseClient


class Client:
    _access_key: str = None
    _access_secret: str = None
    _protocol: str = None
    _endpoint: str = None

    def __init__(
        self, 
        config: upgrade_link_models.Config,
    ):
        self._access_key = config.access_key
        self._access_secret = config.access_secret
        if UtilClient.equal_string(config.protocol, 'HTTPS'):
            self._protocol = 'HTTPS'
        else:
            self._protocol = 'HTTP'
        if UtilClient.empty(config.endpoint):
            self._endpoint = 'api.upgrade.toolsetlink.com'
        else:
            self._endpoint = config.endpoint

    def url_upgrade(
        self,
        request: upgrade_link_models.UrlUpgradeRequest,
    ) -> upgrade_link_models.UrlUpgradeResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/url/upgrade'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/url/upgrade'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                result = UtilClient.assert_as_map(UtilClient.read_as_json(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.UrlUpgradeResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def url_upgrade_async(
        self,
        request: upgrade_link_models.UrlUpgradeRequest,
    ) -> upgrade_link_models.UrlUpgradeResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/url/upgrade'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/url/upgrade'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                result = UtilClient.assert_as_map(await UtilClient.read_as_json_async(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.UrlUpgradeResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def file_upgrade(
        self,
        request: upgrade_link_models.FileUpgradeRequest,
    ) -> upgrade_link_models.FileUpgradeResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/file/upgrade'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/file/upgrade'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                result = UtilClient.assert_as_map(UtilClient.read_as_json(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.FileUpgradeResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def file_upgrade_async(
        self,
        request: upgrade_link_models.FileUpgradeRequest,
    ) -> upgrade_link_models.FileUpgradeResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/file/upgrade'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/file/upgrade'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                result = UtilClient.assert_as_map(await UtilClient.read_as_json_async(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.FileUpgradeResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def apk_upgrade(
        self,
        request: upgrade_link_models.ApkUpgradeRequest,
    ) -> upgrade_link_models.ApkUpgradeResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/apk/upgrade'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/apk/upgrade'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                result = UtilClient.assert_as_map(UtilClient.read_as_json(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.ApkUpgradeResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def apk_upgrade_async(
        self,
        request: upgrade_link_models.ApkUpgradeRequest,
    ) -> upgrade_link_models.ApkUpgradeResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/apk/upgrade'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/apk/upgrade'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                result = UtilClient.assert_as_map(await UtilClient.read_as_json_async(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.ApkUpgradeResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def configuration_upgrade(
        self,
        request: upgrade_link_models.ConfigurationUpgradeRequest,
    ) -> upgrade_link_models.ConfigurationUpgradeResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/configuration/upgrade'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/configuration/upgrade'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                result = UtilClient.assert_as_map(UtilClient.read_as_json(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.ConfigurationUpgradeResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def configuration_upgrade_async(
        self,
        request: upgrade_link_models.ConfigurationUpgradeRequest,
    ) -> upgrade_link_models.ConfigurationUpgradeResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/configuration/upgrade'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/configuration/upgrade'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                result = UtilClient.assert_as_map(await UtilClient.read_as_json_async(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.ConfigurationUpgradeResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def app_report(
        self,
        request: upgrade_link_models.AppReportRequest,
    ) -> upgrade_link_models.AppReportResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/app/report'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/app/report'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                result = UtilClient.assert_as_map(UtilClient.read_as_json(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.AppReportResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def app_report_async(
        self,
        request: upgrade_link_models.AppReportRequest,
    ) -> upgrade_link_models.AppReportResponse:
        request.validate()
        _runtime = {
            'timeout': 10000,
            # 10s 的过期时间
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                # 序列化请求体
                body_str = UtilClient.to_jsonstring(request)
                # 生成请求参数
                timestamp = DarabonbaBaseClient.time_rfc3339()
                nonce = DarabonbaBaseClient.generate_nonce()
                uri = '/v1/app/report'
                access_key = self._access_key
                access_secret = self._access_secret
                # 生成签名
                signature = DarabonbaBaseClient.generate_signature(body_str, nonce, access_secret, timestamp, uri)
                _request.protocol = self._protocol
                _request.method = 'POST'
                _request.pathname = f'/v1/app/report'
                _request.headers = {
                    'host': self._endpoint,
                    'content-type': 'application/json',
                    'x-Timestamp': timestamp,
                    'x-Nonce': nonce,
                    'x-AccessKey': access_key,
                    'x-Signature': signature
                }
                _request.body = body_str
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                result = UtilClient.assert_as_map(await UtilClient.read_as_json_async(_response.body))
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'statusCode': f'{_response.status_code}',
                        'code': f"{result.get('code')}",
                        'message': f"{result.get('msg')}",
                        'docs': f"{result.get('docs')}",
                        'traceId': f"{result.get('traceId')}"
                    })
                return TeaCore.from_map(
                    upgrade_link_models.AppReportResponse(),
                    TeaCore.merge(result)
                )
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)
