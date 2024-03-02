# Base 对象

Base 对象提供了一些操作数据的方法

## 子表

#### getActiveTable

获取当前选中的表格, 返回一个 table 对象

##### 例子

```javascript
 const table = base.getActiveTable();
 output.markdown(`#### ${table.name}`);

```

#### getTables

获取所有的子表

##### 例子

```javascript
const tables = base.getTables();
output.text(tables.length);

```

#### getTableByName

通过一个表格的名称获取一个 table 对象

```javascript
const table = base.getTableByName(tableName: String);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
output.text(table._id);

```

#### addTable

添加一个子表

```javascript
base.addTable(tableName: String);

```

##### 例子

```javascript
base.addTable('New table');

```

#### renameTable

重命名一个子表

```javascript
base.renameTable(oldName: String, newName: String);

```

##### 例子

```javascript
base.renameTable('Old name', 'New name');

```

#### deleteTable

删除一个子表

```javascript
base.deleteTable(tableName: String);

```

##### 例子

```javascript
base.deleteTable('Old table');

```

## 视图

#### getActiveView

获取当前的视图，该方法返回一个 view 对象

##### 例子

```javascript
const view  = base.getActiveView();
output.text(view._id);

```

#### listViews / getViews(deprecated)

获取当前表格的所有视图，并以一个数组的形式返回所有的视图,  其中 getViews 函数已经过期， 新的代码里面可以使用 listViews。

```javascript
const views = base.listViews(table_name);
```

##### 例子

```javascript
const views = base.listViews('Table1');
output.text(views.length);
```

#### getViewByName

通过视图的名称获取表格中的一个视图对象，并返回一个视图对象

```javascript
const view = base.getViewByName(table: Object/String, viewName: String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1'); 
const view = base.getViewByName(table, 'view 1');
output.text(view.name);
```

```javascript
const view = base.getViewByName('Table1', 'view 1');
output.text(view.name);
```

#### addView

一个子表中添加一个视图

```javascript
base.addView(table: Object/String, viewName: String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
base.addView(table, 'view 2');
```

```javascript
base.addView('Table1', 'view 2');
```

#### renameView

重命名一个子表中的一个视图

```javascript
base.renameView(table: Object/String, currentViewName: String, nextViewName: String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
base.renameView(table, 'view1', 'view2');
```

```javascript
base.renameView('Table1', 'view1', 'view2');
```

#### deleteView

删除一个视图

```javascript
base.deleteView(table: Object/String, viewName: String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
base.deleteView(table, 'view2');
```

```javascript
base.deleteView('Table1', 'view2');
```

## 列

#### getColumns

获取一个表格中的所有列，并以一个数组的形式返回所有的列对象

```javascript
const columns = base.getColumns(table: Object/String);
```

###### 例子

```javascript
const table  = base.getTableByName('Table1');
const columns = base.getColumns(table);

column.forEach((column) => {
	output.text(column.name);
})

```

```javascript
const columns = base.getColumns('Table1');
```

#### getShownColumns

获取一个视图中所有显示的列，不包含该视图中已经被隐藏的列, 返回一个数组

```javascript
const columns = base.getShownColumns(table: Object/String, view: Object/String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
const view = base.getViewByName(table, 'view 1');
const columns = base.getShownColumns(table, view);
column.forEach((column) => {
	output.text(column.name);
})
```

```javascript
const columns = base.getShownColumns('Table1', 'view 1');
```

### listColumns

获取表格的所有的列, 通过表格名称和 视图名称获取

```javascript
const columns = base.listColumns(table_name, view_name=null)
```

##### 例子

```
const view_cols = base.listColumns('Table1', 'My_view')
```

#### getColumnByName

通过列的名称获取该列对象

```javascript
const column = base.getColumnByName(table: Object/String, name: String);
```

##### 例子

```javascript
const column = base.getColumnByName(table, 'Column name');
output.text(column.name);
```

```javascript
const column = base.getColumnByName('Table1', 'Column name');
```

#### getColumnsByType

获取该表格中所有特定种类的列

```javascript
const columns = base.getColumnsByType(table: Object/String, type: String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
const columns = base.getColumnsByType(table, 'text');
output.text(column.length);
```

```javascript
const columns = base.getColumnsByType('Table1', 'text');
output.text(column.length);
```

## 行

#### getRows

获取一个视图所有的行，返回一个数组

```javascript
const rows = base.getRows(table_name， view_name);
```

##### 例子

```javascript

const table = base.getTableByName('Table1');
const view = base.getViewByName(table, 'view1');
const rows = base.getRows(table, view);
```

```javascript
const rows = base.getRows('Table1', 'view1');
```

#### getGroupedRows

获取分组视图中的行分组数据

```javascript
base.getGroupedRows(table: Object/String, view: Object/String);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
const view = base.getViewByName(table, '分组视图');
const groupViewRows = base.getGroupedRows(table, view);
```

```javascript
const groupViewRows = base.getGroupedRows('Table1', '分组视图');
```

#### getRow / getRowById(deprecated)

通过一个行的 id 获取行，返回一个行对象，  其中 getRowById 函数已经过期， 新的代码里面可以使用 getRow。

```javascript
const row = base.getRow(table: Object/String, rowId: String);
```

##### 例子

```javascript
const row = base.getRow('Table1', "M_lSEOYYTeuKTaHCEOL7nw");
```

#### deleteRow / deleteRowById(deprecated)

通过一个行的 id 删除当前表格中的该行，其中 deleteRowById 函数已经过期， 新的代码里面可以使用 deleteRow。

```javascript
base.deleteRow(table_name, row_id)
```

##### 例子

```javascript
base.deleteRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### appendRow / addRow(deprecated)

在一个子表中添加一行， 其中 addRow 函数已经过期， 新的代码里面可以使用 appendRow。

```javascript
base.appendRow(table_name, row_data)
```

##### 例子
```javascript
row_data = {
    "Name": "I am new Row"
}
base.appendRow('Table1', row_data)
```

#### updateRow / modifyRow(deprecated)

修改表格中的某一行， 其中 modifyRow 函数已经过期， 新的代码里面可以使用 updateRow。

```javascript
base.updateRow(table_name, row_id, row_data)
```

##### 例子

```javascript
base.updateRow(table_name, row_id, row_data)
// example
row_data = {
    "Name": "T"
}
base.updateRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)

```

#### modifyRows

一次性修改表格中的多行

```javascript
base.modifyRows(table: Object/String, rows: Array, updatedRows: Array);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
const rows = base.getRows('Table1', '默认视图');
const selectedColumnName = '名称';
const selectedRows = [], updatedRows = [];

rows.forEach((row) => {
  if (row[selectedColumnName] === 'name') {
    selectedRows.push(row);
    updatedRows.push({[selectedColumnName]: 'name1'});
  }
});
base.modifyRows(table, selectedRows, updatedRows);
```

## filter

通过一个查询语句, 筛选出表格中符合条件的行, 返回一个 querySet 对象

* [查询语句规范](query-sentences.md)

* [QuerySet](queryset.md)

#### 例子

```javascript
// 过滤出 number列 等于 5 的行, 返回一个 querySet 对象
const querySet = base.filter('Table1', '默认视图', 'number = 5');
```

## Links


#### getLinkedRecords

获取被链接的行的信息。可以一次查询多个行的被链接行的信息。

```javascript
base.getLinkedRecords(tableId, linkColumnKey, rows)
```

其中

* tableId: 子表的 id
* linkColumnKey: 链接列的 key (非 link_id )
* rows: 需要查找链接信息的行的列表，每一列表项包含三个参数 row_id, offset (查找的偏移量, 默认为0)， limit (查找的数量， 默认为10)

##### 例子

```javascript
base.getLinkedRecords('0000', '89o4', [
  {'row_id': 'FzNqJxVUT8KrRjewBkPp8Q', 'limit': 2, 'offset': 0},
  {'row_id': 'Jmnrkn6TQdyRg1KmOM4zZg', 'limit': 20}
])

// 返回的数据结构, 包含被链接的行的 ID 和显示值。每个行所连接的行，按照被链接的行的创建时间顺序以数组形式返回。
{
  'FzNqJxVUT8KrRjewBkPp8Q': [
    {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'},                            
    {'row_id': 'OA6x7CYoRuyc2pT52Znfmw', 'display_value': '3'},
    ...
  ],
  'Jmnrkn6TQdyRg1KmOM4zZg': [
    {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'},     
    {'row_id': 'OA6x7CYoRuyc2pT52Znfmw', 'display_value': '3'},
    ...
  ]
}
```


#### addLink

添加链接，链接其他表记录


```javascript 
base.addLink(linkId, tableName, linkedTableName, rowId, linkedRowId)
```

其中

* linkId: 链接列data属性下的 link_id
* tableName: 链接表的名字
* linkedTableName: 被链接表的名字
* rowId: 链接行 id
* linkedRowId: 被链接行的 id

##### 例子

```javascript
base.addLink('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```

#### removeLink

移除某个链接

```javascript
base.removeLink(linkId, tableName, linkedTableName, rowId, linkedRowId)
```

##### 例子

```javascript
base.removeLink('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```

#### getColumnLinkId

通过列名来获取链接的id

```javascript
base.getColumnLinkId(table_name, column_name)
```

##### 例子

```javascript
base.getColumnLinkId('Table1', '记录')
```

#### updateLinks

移除现有的所有的行的链接, 并添加新链接

```javascript
base.updateLinks(linkId, tableName, linkedTableName, rowId, updatedlinkedRowIds)
```

##### 例子

```javascript
const rows = base.getRows('contact', '默认视图');

// 更新行的链接为 [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id]
base.updateLinks('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id])
```

## query

使用 sql 语句查询一个 base

```javascript
await base.query(sql)

```

#### 例子

######  基础查询

```javascript
const data = await base.query('select name, price, year from Bill')
output.text(data)

```

结果

```javascript
[
	{"name":"Bob","price":"300","year":"2021"},
	{"name":"Bob","price":"300","year":"2019"},
	{"price":"100","year":"2019","name":"Tom"},
	{"name":"Tom","price":"100","year":"2020"},
	{"name":"Tom","price":"200","year":"2021"},
	{"name":"Jane","price":"200","year":"2020"},
	{"name":"Jane","price":"200","year":"2021"}
]

```

###### WHERE

```javascript
const data = await base.query('select name, price from Bill where year = 2021')
output.text(data)

```

结果

```javascript
[
	{"name":"Bob","price":"300"},
	{"name":"Tom","price":"200"},
	{"name":"Jane","price":"200"}
]

```

###### ORDER BY

```javascript
const data = await base.query('select name, price from Bill where year = 2021')
output.text(data)

```

结果

```javascript
[
	{"price":"300","year":2019,"name":"Bob"},
	{"price":"100","year":2019,"name":"Tom"},
	{"name":"Tom","price":"100","year":2020},
	{"price":"200","year":2020,"name":"Jane"},
	{"name":"Bob","price":"300","year":2021},
	{"name":"Tom","price":"200","year":2021},
	{"name":"Jane","price":"200","year":2021}
]

```

###### GROUP BY

```javascript
const data = await base.query('select name, sum(price) from Bill group by name')
output.text(data)

```

结果

```
[
	{"name":"Bob","SUM(price)":600},
	{"SUM(price)":400,"name":"Jane"},
	{"name":"Tom","SUM(price)":400}
]

```

###### DISTINCT

```javascript
const data = await base.query('select distinct name from Bill')
output.text(data)

```

结果

```
[
	{"name":"Bob"},
	{"name":"Jane"},
	{"name":"Tom"}
]

```
