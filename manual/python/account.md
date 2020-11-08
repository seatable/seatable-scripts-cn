# Account

Account 类提供了操作全局 API 的接口，包括

* 列出所有的 Workspace
* 新增/复制/删除 Base
* 获取单个 Base 的访问权限

## 认证

使用 邮箱/密码 进行认证，在调用 Account 提供的 API 前，需要先进行认证

##### 例子

```python
from seatable_api import Account

email = 'xiongxxx@xxx.com'
password = 'xxxxxxx'
server_url = 'https://cloud.seatable.cn/'
account = Account(email, password, server_url)
account.auth()
```


## Workspace

在 SeaTable 中，一个 workspace 是个人的表格的集合或者一个群组的表格的集合。Base 存储在 workspace 中。SeaTable 会为每个账号生成一个个人的 workspace, 每个群组也有一个 workspace。


#### list workspaces

获取您所有 workspace 与其下的 base

```python
account.list_workspaces()
```

##### 例子

```python
account.list_workspaces()
# 返回结果
# {
# 	"workspace_list": [{
# 		"id": 13740,      // workspace的id
# 		"repo_id": "cd9a97a6-9214-4eeb-b609-4295530b9018",
# 		"table_list": [{  // base对象
# 			"id": 24022,
# 			"workspace_id": 13740,
# 			"uuid": "69771c2e-b51e-4fe4-b721-01cd1950e68c",
# 			"name": "q",
# 			"creator": "122",
# 			"modifier": "122",
# 			"created_at": "2020-10-26T14:43:02+08:00",
# 			"updated_at": "2020-10-26T14:43:02+08:00",
# 			"color": null,
# 			"text_color": null,
# 			"icon": null,
# 			"starred": false
# 		}],
# 		"owner_name": "122",
# 		"owner_type": "Personal"
# 	}],
# 	"starred_dtable_list": []
# }
```

## Base

新增/复制/删除 Base，获取一个 Base 访问权限的接口

#### add a base

添加一个 base 到一个 Workspace 

```python
# workspace_id: 如果为None默认添加到自己的workspace
# 如果指定workspace_id则添加到该workspace下
account.add_base(name, workspace_id=None)
```

##### 例子

```python
account.add_base('new-base')
account.add_base('new-base', 35)
```

#### copy a base

复制一个 base 到一个 workspace 中

```python
# 将名为 base_name 的 basee 从 src_workspace 复制到 dst_workspace 中
account.copy_base(src_workspace_id, base_name, dst_workspace_id)
```

##### 例子

```python
account.copy_base(35, 'img-file', 74)
```

#### get a base

获取一个 base 对象

```python
# 获取存在于 id 为 workspac_id 的 workspace 中名为 base_name 的 Base 对象
# Base对象已获得授权，所以不需要调用base.auth()
# with_socket_io: 缺省时False，是否创建socket连接
account.get_base(workspace_id, base_name)
```

```python
base = account.get_base(35, 'img-file')
```
