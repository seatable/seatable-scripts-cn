# Account 对象

Account 提供了授权，列出Workspace，新增/复制Base，获取Base对象

## 授权登录

### auth

使用 用户名/密码 进行登录，如果要进行其他Account下API的操作，请先进行登录操作

##### 例子

```python
from seatable_api import Account

login_name = 'xiongxxx@xxx.com'
password = 'xxxxxxx'
server_url = 'https://cloud.seatable.cn/'
account = Account(login_name, password, server_url)
account.auth()
```

Base对象提供了获取操作Workspace和Base的方法，具体如下

## Workspace

一个Workspace是本人Base的集合或者一个群组Base的集合

#### list workspaces

获取您所有workspaces与其下bases

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

Account对象操作Base，并不是改变Base内部数据，指Base的增删改查

#### add a base

添加一个Base对象到一个Workspace内

```python
# owner: 用于区别您个人的workspace或者群组的workspace
# 如果为None则添加到您自己的workspace中，
# 如果要添加到群组的workspace，则owner应为该workspace的owner字段，详情请参照 list workspaces 返回结果
account.add_base(name, owner=None)
```

##### 例子

```python
account.add_base('new-base')
account.add_base('new-base', '35@seafile_group')
```

#### copy a base

复制一个Base到一个Workspace中

```python
# 将名为base_name的bae从src_workspace复制到dst_workspace中
account.copy_base(src_workspace_id, base_name, dst_workspace_id)
```

##### 例子

```python
account.copy_base(35, 'img-file', 74)
```

#### get a base

获取一个Base对象

```python
# 获取存在于id为workspac_id的workspace中名为base_name的Base对象
account.get_base(workspace_id, base_name)
```

```python
base = account.get_base(35, 'img-file')
base.auth()
# 其他对base的操作
# xxxxxx
```
