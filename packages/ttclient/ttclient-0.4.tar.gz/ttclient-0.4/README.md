[![Version][version-image]][pypi-url]
[![Supported Python Version][py-versions-image]][pypi-url]
[![Downloads][downloads-image]][pypi-url]

---

# TTClient

Клиент для АПИ чата


## INSTALL

Достаточно установить библиотеку ttclient

```
$ pip install ttclient
```


## USAGE

Basic usage

```python
base_client = BaseClient('YOUR_API_SECRET', host='YOUR_API_HOST')
data = await base_client.get('/user/me')
```

Uri template use arguments for formatting, arguments must be string or integer

```python
data = await base_client.get('/core/chat/{}', chat_id)
```

Keywords convert to query string for `GET` and `DELETE` methods
and to json for `POST`, `PUT`, `PATCH`

```python
data = await base_client.get('/core/chat', ids=','.join({chat1_id, chat2_id}))
data = await base_client.post('/core/chat', title='Title', org_visible=True)
data = await base_client.put('/core/chat/{}', chat_id, title='Title', org_visible=True)
data = await base_client.delete('/core/chat/{}', chat_id)
data = await base_client.patch('/user/settings', push_resend=True)
```

Extending client

```python
class MyClient(BaseClient):
    async def my_name(self) -> str:
        data = await self.get('/user/me')
        self.log.debug('Client data %s', str(data))
        return data['name']


client = MyClient('YOUR_API_SECRET', host='YOUR_API_HOST')
name = await client.my_name()
```

<!-- Badges -->
[pypi-url]: https://pypi.org/project/ttclient
[version-image]: https://img.shields.io/pypi/v/ttclient.svg
[py-versions-image]: https://img.shields.io/pypi/pyversions/ttclient.svg
[downloads-image]: https://img.shields.io/pypi/dm/ttclient.svg
