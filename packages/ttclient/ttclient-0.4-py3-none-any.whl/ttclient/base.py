import logging
from collections.abc import Awaitable
from contextlib import suppress
from typing import Any, Literal

import httpx

from .exceptions import (InputDataError, MethodError, NoAccessError,
                         NotFoundError, RedirectError, ServerError,
                         TooManyRequestsError, UnauthorizedError)

HTTP_METHODS = Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE']


class BaseClient:
    '''
        Client for using chat API.

        Basic usage

        ```
            base_client = BaseClient('YOUR_API_SECRET', host='YOUR_API_HOST')
            data = await base_client.get('/user/me')
        ```

        Extending client

        ```
            class MyClient(BaseClient):
                async def my_name(self) -> str:
                    data = await self.get('/user/me')
                    self.log.debug('Client data %s', str(data))
                    return data['name']


            client = MyClient('YOUR_API_SECRET', 'YOUR_API_HOST')
            name = await client.my_name()
        ```
    '''
    __secret__: str = ''
    host: str = ''
    log: logging.Logger = logging.getLogger('ttclient')

    def __init__(self, secret: str, host: str) -> None:
        self.__secret__ = secret
        self.host = f'https://{host}'

    def __repr__(self) -> str:
        return f'Client [{self.host}]' + (' with ' if self.__secret__ else ' no ') + 'secret'

    def http_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(headers={'X-APIToken': self.__secret__})

    async def api_call(self, method: HTTP_METHODS, uri: str, **data: Any) -> dict:
        '''
            Call the API and handling the answer.

            ```
                data = await client.api_call('GET', '/core/chat', ids=1)

                try:
                    await client.api_call('PUT', '/core/chat/1', title='Title')
                except NoAccessError:
                    ...
                except NotFoundError:
                    ...
            ```
        '''
        async with self.http_client() as client:
            result = {}

            if method in {'POST', 'PUT', 'PATCH'}:
                resp = await client.request(method, f'{self.host}{uri}', json=data or {})
            else:
                resp = await client.request(method, f'{self.host}{uri}', params=data or None)

            self.log.info('CALL API %s %s: %s', method, uri, resp.status_code)

            with suppress(Exception):
                result = resp.json()

            match resp.status_code:
                case 400:
                    raise InputDataError(method, uri, data, result, resp.status_code)
                case 401:
                    raise UnauthorizedError(method, uri, data, result, resp.status_code)
                case 403:
                    raise NoAccessError(method, uri, data, result, resp.status_code)
                case 404:
                    raise NotFoundError(method, uri, data, result, resp.status_code)
                case 405:
                    raise MethodError(method, uri, data, result, resp.status_code)
                case 429:
                    raise TooManyRequestsError(method, uri, data, result, resp.status_code)
                case 301 | 302:
                    raise RedirectError(method, uri, data, result, resp.status_code)
                case 500 | 502 | 503 | 504:
                    raise ServerError(method, uri, data, result, resp.status_code)

            return result

    def get(self, uri: str, *uri_args: int | str, **data: Any) -> Awaitable[dict]:
        '''
            Fetching data

            ```
                data = await client.get('/core/chat', ids=1)
                data = await client.get('/core/chat/{}', chat_id)
            ```
        '''
        return self.api_call('GET', uri.format(*uri_args), **data)

    def post(self, uri: str, *uri_args: int | str, **data: Any) -> Awaitable[dict]:
        '''
            Create objects, call actions

            ```
                data = await client.post('/core/chat', title='Title')
                await client.post('/core/chat/{}/enter', chat_id)
                await client.post('/msg/post/{}/{}/complaint', chat_id, post_no)
            ```
        '''
        return self.api_call('POST', uri.format(*uri_args), **data)

    def put(self, uri: str, *uri_args: int | str, **data: Any) -> Awaitable[dict]:
        '''
            Update objects

            ```
                data = await client.put('/core/chat/{}', chat_id, title='Title')
                await client.put('/msg/post/{}/{}', chat_id, post_no, text='text')
            ```
        '''
        return self.api_call('PUT', uri.format(*uri_args), **data)

    def patch(self, uri: str, *uri_args: int | str, **data: Any) -> Awaitable[dict]:
        '''
            Partial update

            ```
                data = await client.patch('/user/settings', push_resend=True)
            ```
        '''
        return self.api_call('PATCH', uri.format(*uri_args), **data)

    def delete(self, uri: str, *uri_args: int | str, **data: Any) -> Awaitable[dict]:
        '''
            Delete object, undo actions

            ```
                await client.delete('/core/chat/{}', chat_id)
            ```
        '''
        return self.api_call('DELETE', uri.format(*uri_args), **data)
