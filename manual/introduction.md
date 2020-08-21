# SeaTable 脚本编程手册

SeaTable 脚本使用 Javascript 语言编写。一个脚本一般用于表格中数据的处理。脚本可以在用户的浏览器中或者后台运行。(目前仅支持在用户的浏览器中运行)

脚本执行器提供了两个对象供你使用:

1. base 对象。一个 base 代表了 SeaTable 中的一个表格。通过 base 对象可以操作表格中的数据。
2. output 对象。用于输出结果。

一个 base 包含多个子表 (Table)。每个子表包含多个行。行中的单元格由对应的列类型来规定数据格式。具体可以参考 [数据结构](data-structure.md)

## base 对象

base 对象提供了一个提供操作表格的入口。

下面为 base 对象提供的方法。

### 子表

#### getActiveTable

获取当前选中的表格, 返回一个 table 对象

##### 例子

```javascript
 const table = base.getActiveTable();
 // 打印当前表格的名称 
 output.markdown(`#### ${table.name}`);

```

#### getTables

获取所有的子表

##### 例子

```javascript
const tables = base.getTables();

// 打印表格的数量
output.text(tables.length);

```

#### getTableByName

通过一个表格的名称获取一个 table 对象

##### 例子

```javascript
const table = base.getTableByName(tableName: String);
// 打印表格的 id
output.text(table._id);

```

#### addTable

添加一个子表

##### 例子

```javascript
// 添加一个名称为 new table 的字表
base.addTable('new table');

```

#### renameTable

重命名一个子表

##### 例子

```javascript
base.renameTable(currentTableName: String, nextTableName: String);
// 将名称为 new table 的字表重命名为 old table
base.renameTable('new table', 'old table');

```

#### deleteTable

删除一个子表

##### 例子

```javascript
base.deleteTable(tableName: String);
// 删除一个名称为 old table 的子表
base.deleteTable('old table');

```

### 视图

#### getActiveView

获取当前的视图，该方法返回一个 view 对象

##### 例子

```javascript
const view  = base.getActiveView();
// 打印当前 view 的 id
output.text(view._id);

```

#### getViews

获取当前表格的所有视图，并以一个数组的形式返回所有的视图

##### 例子

```javascript
const views = base.getViewByName(table: Object);
// 打印当前表的的 view 的数量
output.text(views.length);

```

#### getViewByName

通过视图的名称获取表格中的一个视图对象，并返回一个视图对象

##### 例子

```javascript
const view = base.getViewByName(table: Object, viewName: String);
// 打印当前 view 的 id
output.text(views.length);

```

#### addView

一个子表中添加一个视图

##### 例子

```javascript
base.addView(tableName: String, viewName: String);
// 在名称为 table 的子表中添加一个 view1 的视图
base.addView('table', 'view1');

```

#### renameView

重命名一个字表中的一个视图

##### 例子

```javascript
base.renameView(tableName: String, currentViewName: String, nextViewName: String);
// 将 table 子表中的视图 view1 重命名为 view2
base.renameView('table', 'view1', 'view2');

```

#### deleteView

删除一个视图

##### 例子

```javascript
base.deleteView(tableName: String, viewName: String);
// 将视图 view2 删除
base.deleteView('table', 'view2');

```

### 列

#### getColumns

获取一个表格中的所有列，并以一个数组的形式返回所有的列对象

###### 例子

```javascript
const columns = base.getColumns(table: Object);

// 打印表格中每一列的名称
column.forEach((column) => {
	output.text(column.name);
})

```

#### getShownColumns

获取一个视图中所有显示的列，不包含该视图中已经被隐藏的列, 返回一个数组

##### 例子

```javascript
const columns = base.getShownColumns(table: Object, view: Object);
// 打印表格中没有隐藏的每一列的名称
column.forEach((column) => {
	output.text(column.name);
})

```

#### getColumnByName

通过列的名称获取该列对象

##### 例子

```javascript
const column = base.getColumnByName(table: Object, name: String);
// 打印该列的名称
output.text(column.name);

```

#### getColumnsByType

获取该表格中所有特定种类的列

##### 例子

```javascript
const columns = base.getColumnsByType(table: Object, type: String);
// 查看表格中某一类型列的数量
output.text(column.length);

```

### 行

#### getViewRows

获取一个视图所有的行，返回一个数组

##### 例子

```javascript
const rows = base.getViewRows(view: Object, table: Object);

```

##### getRowById

通过一个行的 id 获取行，返回一个行对象

##### 例子

```javascript
const row = base.getRowById(table: Object, rowId: String);

// 获取该行中'名称'列的内容
const column = base.getColumnByName(table: Object, '名称');
const columnKey = column.key;
const value = row.columnKey;

```

#### deleteRowById

通过一个行的 id 删除当前表格中的该行

##### 例子

```javascript
base.deleteRowById(table: Object, rowId: String);

```

#### addRow

在一个子表中添加一行

```javascript
base.addRow(tableName: String, rowData: Object, viewName?: String)

// use case
base.addRow('Table1', {'名称': '小强', '年龄': '18'});

// use case
base.addRow('Table1', {'名称': '小强', '年龄': '18'}, 'Default View');
```

#### modifyRow

修改表格中的某一行

##### 例子

```javascript
base.modifyRow(table: Object, row: Object, updateRowData: Object);
// 修改名称为 table 的表格中最后一行的名称列和 number 列的内容为 '1111', 和 100
const table = base.getTableByName('table');
const rows = table.rows;
const lastRow = rows[rows.length - 1];
base.modifyRow(table, lastRow, {'名称': '1111', number: 100});

```

#### getGroupRows

获取分组视图中的行分组数据

##### 例子

```javascript
base.getGroupRows(view: Object, table: Object);
// 获取某个分组视图的分组数据
const table = base.getTableByName('table');
const view = base.getViewByName(table, '分组视图');
const groupViewRows = base.getGroupRows(view, table);

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