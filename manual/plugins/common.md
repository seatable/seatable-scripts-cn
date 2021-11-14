# Common api

## getRelatedUsers

获取当前 base 关联的其他用户(表格的协作人, 表的被分享人等)

```javascript
dtable.getRelatedUsers()
```

例子

```javascript
const collaborators = dtable.getRelatedUsers();
```

## getCollaboratorsName

获取协作者的名字列表

```javascript
dtable.getCollaboratorsName(collaborators, value)
```

其中

* collaborators: base 协作人列表
* value: 协作者列的邮箱列表

例子

```javascript
const collaborators = dtable.getRelatedUsers();
const value = ['abc@seafile.com', 'shun@seafile.com'];
const name = dtable.getCollaboratorsName(collaborators, value); // 'abc, shun'
```

## getTableFormulaResults

获取子表计算公式列的数据

```javascript
dtable.getTableFormulaResults(table, rows)
```

其中

* table: 子表对象
* rows: 需要获取 计算公式列相关数据的行数据

例子

```javascript
const tableName = 'tableName';
const viewName = 'viewName';
const table = dtable.getTableByName(tableName);
const view = dtable.getViewByName(table, viewName);
const rows = dtable.getViewRows();

const formulaResult = dtable.getTableFormulaResults(table, rows);
```

## getViewRowsColor

获取视图中行数据的颜色属性

```javascript
dtable.getViewRowsColor(rows, view, table)
```

其中

* rows: 需要获取 颜色属性 的行数据
* view: 视图对象
* table: 子表对象

例子

```javascript
const tableName = 'tableName';
const viewName = 'viewName';
const table = dtable.getTableByName(tableName);
const view = dtable.getViewByName(table, viewName);
const rows = dtable.getViewRows();

const formulaResult = dtable.getViewRowsColor(rows, view, table);
```

## getLinkCellValue

获取子表行数据关联其他表格的行数据的 id 列表

```javascript
dtable.getLinkCellValue(linkId, tableId, otherTableId, rowId)
```

其中

* linkId: link 列对应的 link_id 值
* tableId: 当前表格的 id 值
* otherTableId: 关联表格的 id 值
* rowId: 当前表格中行的 id 值

例子

```javascript
const tableName = 'tableName';
const table = dtable.getTableByName(tableName);


const rows = table.rows;
const row = rows[0];

const columnName = 'linkColumn';
const linkColumn = dtable.getColumnByName(table, columnName);
const { link_id, table_id, other_table_id, display_column_key } = linkColumn.data;
const linkedTaleId = table._id === table_id ? other_table_id : table_id;

const linkedRowIds = dtable.getLinkCellValue(link_id, table._id, linkedTableId, row._id);
```


## getLinkDisplayString

获取 link 列关联行的内容值

```javascript
dtable.getLinkDisplayString(linkedRowIds, linkedTable, displayColumnKey)
```

其中

* linkedRowIds: 关联的行列表
* linkedTable: 关联的子表对象
* displayColumnKey: 关联的列对象

例子

```javascript
const tableName = 'tableName';
const table = dtable.getTableByName(tableName);


const rows = table.rows;
const row = rows[0];

const columnName = 'linkColumn';
const linkColumn = dtable.getColumnByName(table, columnName);
const { link_id, table_id, other_table_id, display_column_key } = linkColumn.data;
const linkedTaleId = table._id === table_id ? other_table_id : table_id;

const linkedRowIds = dtable.getLinkCellValue(link_id, table._id, linkedTableId, row._id);
const linkedTable = dtable.getTableById(linkedTableId);

const results = dtable.getLinkDisplayString(linkedRowIds, linkedTable, display_column_key);
```

## getNumberDisplayString

获取 number 列的字符串显示(按照不同的format返回用户数据)

```javascript
dtable.getNumberDisplayString(value, columnData)
```

其中

* value: number 类型列对应的 value 值
* columnData: number 类型列 对应的 column 的 data 配置属性

例子

```javascript
const tableName = 'tableName';
const table = dtable.getTableByName(tableName);
const columnName = 'dateColumn';
const column = dtable.getColumnByName(table, columnName);

const value = 190203;
const name = dtable.getNumberDisplayString(value, column.data);
```

## getGeolocationDisplayString

获取 geolocation 列的字符串显示(按照不同的配置参数返回用户数据)

```javascript
dtable.getGeolocationDisplayString(value, columnData)
```

其中

* value: geolocation 类型列对应的 value 值
* columnData: geolocation 类型列 对应的 column 的 data 配置属性

例子

```javascript
const tableName = 'tableName';
const table = dtable.getTableByName(tableName);
const columnName = 'dateColumn';
const column = dtable.getColumnByName(table, columnName);

const value = {city: "安庆市", detail: "nide" ,district: "迎江区", province: "安徽省"};
const name = dtable.getGeolocationDisplayString(value, column.data);
```

## getDurationDisplayString

获取 duration 列的字符串显示(按照不同的配置参数返回用户数据)

```javascript
dtable.getDurationDisplayString(value, columnData)
```

其中

* value: duration 类型列对应的 value 值
* columnData: duration 类型列 对应的 column 的 data 配置属性

例子

```javascript
const tableName = 'tableName';
const table = dtable.getTableByName(tableName);
const columnName = 'dateColumn';
const column = dtable.getColumnByName(table, columnName);

const value = '12:30';
const name = dtable.getDurationDisplayString(value, column.data);
```

## getDateDisplayString

获取 date 列的字符串显示(按照不同的配置参数返回用户数据)

```javascript
dtable.getDateDisplayString(value, columnData)
```

其中

* value: date 类型列对应的 value 值
* columnData: date 类型列 对应的 column 的 data 配置属性

例子

```javascript
const tableName = 'tableName';
const table = dtable.getTableByName(tableName);
const columnName = 'dateColumn';
const column = dtable.getColumnByName(table, columnName);

const value = 'YYYY-MM-DD';
const name = dtable.getDateDisplayString(value, column.data);
```
