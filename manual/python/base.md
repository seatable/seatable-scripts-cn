# Base 对象

Base 代表一个表格。你可以用两种方法来获取读写一个 base 的授权。一个是使用单个表格的 api token, 这个 token 可以在网页端直接生成。在云端环境下从 context.api_token 直接读取。

还有一个方法是使用账号名和密码来初始化一个 Account 对象，然后调用 Account 的接口来获取一个 base 对象。第一种方法更加安全一些。

## 获取授权

使用表格的 API Token 来获取一个 base 的访问授权。

##### 例子

```python
from seatable_api import Base, context

server_url = context.server_url or 'https://cloud.seatable.cn'
api_token = context.api_token or 'c3c75dca2c369849455a39f4436147639cf02b2d'

base = Base(api_token, server_url)
base.auth()
```

## Metadata

#### Get metadata

##### 例子

```python
base.get_metadata()
```

返回结果

```python
{
	'tables': [{
		'_id': '4krH',
		'name': '联系人',
		'is_header_locked': False,
		'columns': [{
			'key': '0000',
			'type': 'text',
			'name': '名称',
			'editable': True,
			'width': 200,
			'resizable': True,
			'draggable': True,
			'data': None,
			'permission_type': '',
			'permitted_users': []
		}, {
			'key': 'M31F',
			'type': 'text',
			'name': '邮箱',
			'editable': True,
			'width': 200,
			'resizable': True,
			'draggable': True,
			'data': None,
			'permission_type': '',
			'permitted_users': []
		}],
		'views': [{
			'_id': '0000',
			'name': '默认视图',
			'type': 'table',
			'is_locked': False,
			'filter_conjunction': 'And',
			'filters': [],
			'sorts': [],
			'groupbys': [],
			'group_rows': [],
			'groups': [],
			'colorbys': {},
			'hidden_columns': [],
			'rows': [],
			'formula_rows': {},
			'link_rows': {},
			'summaries': {},
			'colors': {}
		}]
	}]
}
```

## Table

#### add table

在 base 中添加子表

```python
base.add_table(table_name, lang='en')
```

其中

* table_name: 需要添加的子表名称
* lang：语言， 默认 en ， 目前支持英文 ( en )和中文 ( zh-cn )

##### 例子

```python
base.add_table('项目调查表', lang='zh-cn')
```

#### 

## Base 上的操作

Base 对象提供了操作行和列，上传下载文件等的接口，请参考文档

* [Rows](rows.md)
* [Links](links.md)
* [Columns](columns.md)
* [Files](files.md)



## 授权过期的处理方式

一些情况下， 我们需要把表格的读写逻辑放入到 while 或者 for 循环里面长期运行。在运行过程中授权可能会因为授权过期而导致程序中断，我们在此提供了一个异常 `AuthExpiredError`， 可以通过捕获该异常，来进行重新授权，参考如下

```python
from seatable_api import Base, context
from seatable_api.exception import AuthExpiredError

server_url = context.server_url or 'https://cloud.seatable.cn'
api_token = context.api_token or 'c3c75dca2c369849455a39f4436147639cf02b2d'

base = Base(api_token, server_url)
base.auth()

while True:
    try:
        base.append_row('Table1', {"xxx":"xxx"})
        ...
    except AuthExpiredError:
       base.auth()
```

