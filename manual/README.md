# SeaTable 脚本编程手册

SeaTable 脚本使用 Javascript 语言编写。一个脚本一般用于表格中数据的处理。脚本可以在用户的浏览器中或者后台运行。(目前仅支持在用户的浏览器中运行)

脚本执行器提供了两个对象供你使用:

1. base 对象。一个 base 代表了 SeaTable 中的一个表格。通过 base 对象可以操作表格中的数据。
2. output 对象。用于输出结果。

一个 base 包含多个子表 (Table)。每个子表包含多个行。行中的单元格由对应的列类型来规定数据格式。具体可以参考

* [数据结构](data-structure.md)

## base 对象

base 对象提供了一个提供操作表格的入口。

下面为 base 对象提供的方法。

### 子表

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

### 视图

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
const views = base.getViews(table: Object);

```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
const views = base.getViews(table);
output.text(views.length);

```

#### getViewByName

通过视图的名称获取表格中的一个视图对象，并返回一个视图对象

```javascript
const view = base.getViewByName(table: Object, viewName: String);

```

##### 例子

```javascript
const table  = base.getTableByName('Table1'); 
const view = base.getViewByName(table, 'view 1');
output.text(view.name);

```

#### addView

一个子表中添加一个视图

```javascript
base.addView(table: Object, viewName: String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
base.addView(table, 'view 2');
```

#### renameView

重命名一个子表中的一个视图

```javascript
base.renameView(table: Object, currentViewName: String, nextViewName: String);

```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
base.renameView(table, 'view1', 'view2');

```

#### deleteView

删除一个视图

```javascript
base.deleteView(table: Object, viewName: String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
base.deleteView(table, 'view2');

```

### 列

#### getColumns

获取一个表格中的所有列，并以一个数组的形式返回所有的列对象

```javascript
const columns = base.getColumns(table: Object);

```

###### 例子

```javascript
const table  = base.getTableByName('Table1');
const columns = base.getColumns(table);

column.forEach((column) => {
	output.text(column.name);
})

```

#### getShownColumns

获取一个视图中所有显示的列，不包含该视图中已经被隐藏的列, 返回一个数组

```javascript
const columns = base.getShownColumns(table: Object, view: Object);
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

#### getColumnByName

通过列的名称获取该列对象

```javascript
const column = base.getColumnByName(table: Object, name: String);
```

##### 例子

```javascript
const column = base.getColumnByName(table, 'Column name');
output.text(column.name);

```

#### getColumnsByType

获取该表格中所有特定种类的列

```javascript
const columns = base.getColumnsByType(table: Object, type: String);
```

##### 例子

```javascript
const table  = base.getTableByName('Table1');
const columns = base.getColumnsByType(table, 'text');
output.text(column.length);

```

### 行

#### getRows

获取一个视图所有的行，返回一个数组

```javascript
const rows = base.getRows(table: Object, view: Object);

```

##### 例子

```javascript

const table = base.getTableByName('Table1');
const view = base.getViewByName(table, 'view1');
const rows = base.getRows(table, view);
```

#### getGroupedRows

获取分组视图中的行分组数据

```javascript
base.getGroupedRows(table: Object, view: Object);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
const view = base.getViewByName(table, '分组视图');
const groupViewRows = base.getGroupedRows(table, view);

```

##### getRowById

通过一个行的 id 获取行，返回一个行对象

```javascript
const row = base.getRowById(table: Object, rowId: String);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
const row = base.getRowById(table, "M_lSEOYYTeuKTaHCEOL7nw");
```

#### deleteRowById

通过一个行的 id 删除当前表格中的该行

```javascript
base.deleteRowById(table: Object, rowId: String);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
base.deleteRowById(table, 'M_lSEOYYTeuKTaHCEOL7nw');
```

#### addRow

在一个子表中添加一行

```javascript
base.addRow(table: Object, rowData: Object, viewName?: String)
```

##### 例子
```javascript
const table = base.getTableByName('Table1');
base.addRow(table, {'名称': '小强', '年龄': '18'});
base.addRow(table, {'名称': '小强', '年龄': '18'}, 'Default View');

```

#### modifyRow

修改表格中的某一行

```javascript
base.modifyRow(table: Object, row: Object, updateRowData: Object);
```

##### 例子

```javascript
const table = base.getTableByName('Table1');
const row = base.getRowById(table, "M_lSEOYYTeuKTaHCEOL7nw");
base.modifyRow(table, row, {'Name': 'new name', 'number': 100});
```

## base.utils 工具对象

### formatDate

格式化日期, 返回一个 ‘YYYY-MM-DD’ 格式的日期

##### 例子

```javascript
let date = new Date();
let formatDate = base.utils.formatDate(date);

output.text(formatDate); // 2020-08-20
```

### formatDateWithMinutes

格式化日期, 返回一个 ‘YYYY-MM-DD HH:mm’ 格式的日期

##### 例子

```javascript
let date = new Date();
let formatDate = base.utils.formatDateWithMinutes(date);

output.text(formatDate); // 2020-08-20 14:00
```

## output 对象

output 对象用于输出内容。支持输出 text 和 Markdown 两种格式。

### Text

用于在插件的控制台输出文本信息

```javascript
const table = base.getActiveTable();
// 输出该表格的名称
output.text(table.name);

```

### Markdown

用于在插件的控制台输出 markdown 格式的内容

```javascript
const table = base.getActiveTable()；

// 将该表格的名称以一个五级表题的格式输入到插件控制台
output.markdown(`##### ${table.name}`)；

```
