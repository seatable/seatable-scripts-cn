# Base 对象

Base 代表一个表格。你可以用表格的 api token 获取读写 base 的授权, 这个 token 可以在网页端直接生成。

## 获取授权

使用表格的 API Token 来获取一个 base 的访问授权。

##### 例子

```javascript
import { Base } from 'seatable-api';

const config = {
  server: 'https://cloud.seatable.cn',
  APIToken: 'c3c75dca2c369849455a39f4436147639cf02b2d'
};

const base = new Base(config);
await base.auth()
```

## Metadata

#### Get metadata

获取 base 的 metadata 信息

```javascript
base.getMetadata();
```

##### 例子

```javascript
const metadata = await base.getMetadata();
```

返回结果

```javascript
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

####  Get tables

获取 base 中的表格信息

```javascript
base.getTables()
```

##### 例子

```javascript
const tables = await base.getTables();
```

####  Get table by name

通过名称获取子表

```javascript
base.getTableByName(table_name);
```

##### 例子

```javascript
const table = await base.getTableByName('Table1')
```

#### Add table

在 base 中添加子表

```javascript
base.addTable(table_name, lang='en')
```

其中

* lang：语言， 默认 en ， 目前支持英文 ( en )和中文 ( zh-cn )

##### 例子

```javascript
await base.addTable('项目调查表', lang='zh-cn')
```

####  Rename table

获取 base 中的表格信息

```javascript
base.renameTable(old_name, new_name)
```

##### 例子

```javascript
await base.renameTable('Table_Add1', 'New_Table_Add1');
```

####  Delete table

删除一个子表

```javascript
base.deleteTable(table_name)
```

##### 例子

```javascript
await base.deleteTable('Table1')
```

## Base 上的操作

Base 对象提供了操作行和列的接口，请参考文档

* [Rows](rows.md)
* [Links](links.md)
* [Columns](columns.md)
* [Query with SQL](query.md)

