# Columns

## getColumnsByType

获取子表中所有类型一样的列内容

```javascript
getColumnsByType(columns, type);
```

其中

* columns: 子表中所有的列
* type: 获取列的类型

### 例子
```javascript
import { CellType, getTableById, getColumnsByType } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)

const columns = window.dtableSDK.getColumns(table); // const columns = table.columns;

const columnType = CellType.TEXT;
const sameTypeColumns = getColumnsByType(columns, columnType);
```

## getColumnByName

通过 name 获取列内容

```javascript
getTableColumnByName(table, columnName);
```

其中

* table: 子表对象
* columnName: 获取列的名字

### 例子
```javascript
import { CellType, getTableById, getColumnByName } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)

const columns = window.dtableSDK.getColumns(table); // const columns = table.columns;

const columnName = 'columnName';
const column = getTableColumnByName(columns, columnName);
```

## getColumnByKey

通过 key 获取列内容

```javascript
getTableColumnByKey(table, columnKey);
```

其中

* table: 子表对象
* columnKey: 获取列的 key 值

### 例子
```javascript
import { CellType, getTableById, getTableColumnByKey } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)

const columnKey = '0000';
const column = getTableColumnByKey(table, columnKey);
```
