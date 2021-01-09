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

##### 例子

```python
account.list_workspaces()
```

返回结果

```python
{
 "workspace_list": [{
 		"id": 13740,      # workspace的id
 		"repo_id": "cd9a97a6-9214-4eeb-b609-4295530b9018",
 		"table_list": [{  # base对象
 			"id": 24022,
 			"workspace_id": 13740,
 			"uuid": "69771c2e-b51e-4fe4-b721-01cd1950e68c",
			"name": "q",
 			"creator": "122",
 			"modifier": "122",
 			"created_at": "2020-10-26T14:43:02+08:00",
 			"updated_at": "2020-10-26T14:43:02+08:00",
 			"color": null,
 			"text_color": null,
 			"icon": null,
 			"starred": false
 		}],
 		"owner_name": "122",
 		"owner_type": "Personal"
 	}],
 	"starred_dtable_list": []
}
```



## Base

新增/复制/删除 Base，获取一个 Base 访问权限的接口

#### add a base

添加一个 base 到一个 Workspace 

```python
account.add_base(name, workspace_id=None)
```

其中

* workspace_id: 添加到指定的工作区，如果为 None 则默认添加到自己的工作区

##### 例子

```python
account.add_base('new-base')
account.add_base('new-base', 35)
```

#### copy a base

复制一个 base 到一个 workspace 中

```python
account.copy_base(src_workspace_id, base_name, dst_workspace_id)
```

其中

* src_workspace_id: 源工作区 id
* dst_workspace_id: 目标工作区 id
* base_name: base 的名称

即将名为 base_name 的 base 从源工作区复制到目标工作区

##### 例子

```python
account.copy_base(35, 'img-file', 74)
```

#### get a base

获取一个 base 对象

```python
# 获取存在于 id 为 workspac_id 的 workspace 中名为 base_name 的 Base 对象
# Base对象已获得授权，所以不需要调用 base.auth()
account.get_base(workspace_id, base_name)
```

##### 例子

```python
base = account.get_base(35, 'img-file')
```

