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

#### getViews

获取当前表格的所有视图，并以一个数组的形式返回所有的视图

```javascript
const views = base.getViews(table: Object/String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
const views = base.getViews(table);
output.text(views.length);
```

```javascript
const views = base.getViews('Table1');
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
const rows = base.getRows(table: Object/String, view: Object/String);
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

##### getRowById

通过一个行的 id 获取行，返回一个行对象

```javascript
const row = base.getRowById(table: Object/String, rowId: String);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
const row = base.getRowById(table, "M_lSEOYYTeuKTaHCEOL7nw");
```

```javascript
const row = base.getRowById('Table1', "M_lSEOYYTeuKTaHCEOL7nw");
```

#### deleteRowById

通过一个行的 id 删除当前表格中的该行

```javascript
base.deleteRowById(table: Object/String, rowId: String);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
base.deleteRowById(table, 'M_lSEOYYTeuKTaHCEOL7nw');
```

```javascript
base.deleteRowById('Table1', 'M_lSEOYYTeuKTaHCEOL7nw');
```

#### addRow

在一个子表中添加一行

```javascript
base.addRow(table: Object/String, rowData: Object, viewName?: String)
```

##### 例子
```javascript
const table = base.getTableByName('Table1');
base.addRow(table, {'名称': '小强', '年龄': '18'});
base.addRow(table, {'名称': '小强', '年龄': '18'}, 'Default View');
```

```javascript
base.addRow('Table1', {'名称': '小强', '年龄': '18'});
base.addRow('Table1', {'名称': '小强', '年龄': '18'}, 'Default View');
```

#### modifyRow

修改表格中的某一行

```javascript
base.modifyRow(table: Object/String, row: Object, updateRowData: Object);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
const row = base.getRowById(table, "M_lSEOYYTeuKTaHCEOL7nw");
base.modifyRow(table, row, {'Name': 'new name', 'number': 100});
```

```javascript
const row = base.getRowById('Table1', "M_lSEOYYTeuKTaHCEOL7nw");
base.modifyRow('Table1', row, {'Name': 'new name', 'number': 100});
```

#### modifyRows

一次性修改表格中的多行

```javascript
base.modifyRow(table: Object/String, rows: Array, updatedRows: Array);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
const rows = base.getRows('Table1', '默认视图');
const selectedColumnName = '名称';
const selectedRows = [], updatedRows = [];

rows.forEach((row) => {
  if (row[columnName] === 'name') {
    selectedRosws.push(row);
    updatedRows.push({columnName: 'name1'});
  }
});
base.modifyRow(table, selectedRows, updatedRows);
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

移除现有的所有的行的链接, 并更新

```javascript
base.utils.updateLinks(linkId, tableName, linkedTableName, rowId, updatedlinkedRowIds)
```

##### 例子

```javascript
const rows = base.getRows('contact', '默认视图');

// 更新行的链接为 [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id]
base.utils.updateLinks('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id])
```