# Common api

## getRelatedUsers

获取当前 base 关联的其他用户(表格的协作人, 表的被分享人等)

```javascript
window.dtableSDK.getRelatedUsers()
```

例子

```javascript
const collaborators = window.dtableSDK.getRelatedUsers();
```

## getTableFormulaResults

获取子表计算公式列的数据

```javascript
window.dtableSDK.getTableFormulaResults(table, rows)
```

其中

* table: 子表对象
* rows: 需要获取 计算公式列相关数据的行数据

例子

```javascript
import { getTableById, getViewById } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const viewId = '0000';
const view = getViewById(table.views, viewId);

const rows = window.dtableSDK.getViewRows(view, table);

const formulaResult = window.dtableSDK.getTableFormulaResults(table, rows);
```

## getViewRowsColor

获取视图中行数据的颜色属性

```javascript
window.dtableSDK.getViewRowsColor(rows, view, table)
```

其中

* rows: 需要获取 颜色属性 的行数据
* view: 视图对象
* table: 子表对象

例子

```javascript
import { getTableById, getViewById } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const viewId = '0000';
const view = getViewById(table.views, viewId);

const rows = window.dtableSDK.getViewRows(view, table);

const rowsColor = window.dtableSDK.getViewRowsColor(rows, view, table);
```
