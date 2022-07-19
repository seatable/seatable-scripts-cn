# Websocket

## 实时获取数据更新通知

利用 Websocket，您可以像 SeaTable 网页端一样实时获取 Base 的数据更新通知

##### 例子

```python
from seatable_api import Base

server_url = 'https://cloud.seatable.cn'
api_token = 'c3c75dca2c369849455a39f4436147639cf02b2d'

base = Base(api_token, server_url)
base.auth(with_socket_io=True)

base.socketIO.wait()
```

当 Base 有数据更新时，命令行中将输出以下内容

```log
2022-07-19 11:48:37.803956 [ SeaTable SocketIO connection established ]
2022-07-19 11:48:39.953150 [ SeaTable SocketIO on UPDATE_DTABLE ]
{"op_type":"insert_row","table_id":"0000","row_id":"YFK9bD1XReSuQ7WP1YYjMA","row_insert_position":"insert_below","row_data":{"_id":"RngJuRa0SMGXyiA-SHDiAw","_participants":[],"_creator":"seatable@seatable.com","_ctime":"","_last_modifier":"seatable@seatable.com","_mtime":""},"links_data":{}}
```

### 获取数据更新，自定义后续的操作

通过重写 UPDATE_DTABLE 事件，您可以自定义后续的操作

##### 例子

```python
import json
from seatable_api import Base
from seatable_api.constants import UPDATE_DTABLE

server_url = 'https://cloud.seatable.cn'
api_token = 'c3c75dca2c369849455a39f4436147639cf02b2d'

def on_update(data, index, *args):
    try:
        operation = json.loads(data)
        print(operation)
        op_type = operation['op_type']
        table_id = operation['table_id']
        row_id = operation['row_id']
        # ... do something
    except Exception as e:
        print(e)

base = Base(api_token, server_url)
base.auth(with_socket_io=True)

base.socketIO.on(UPDATE_DTABLE, on_update)
base.socketIO.wait()
```
