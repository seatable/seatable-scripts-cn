# Rows

## getRowById

通过 id 获取子表的相关行数据

```javascript
getRowById(table, rowId);
```

其中

* table: 子表对象
* rowId: 查找行的 id 值

例子

```javascript
import { getTableById, getRowById } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const rowId = 'aaaa';

const rows = getRowById(table, rowId);
```

## getRowsByIds

通过 id 列表获取子表的相关行数据

```javascript
getRowsByIds(tableId, rowIds);
```

其中

* table: 子表对象
* rowIds: 查找行的 id 列表

例子

```javascript
import { getTableById, getRowsByIds } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const rowIds = ['aaa', 'bbb', 'cccc', 'dddd'];

const rows = getRowsByIds(table, rowIds);
```
