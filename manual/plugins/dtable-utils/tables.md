# Tables

## getTableById

通过 id 获取子表内容

```javascript
getTableById(tables, tableId);
```

其中

* tables: Base 中所有的表格
* tableId: 子表的 id 值

例子

```javascript
import { getTableByName } from 'dtable-utils';

const tables = window.dtableSDK.getTables();
const tableId = 'tableId';
const table = getTableByName(tables, tableId)
```

## getTableByName

通过 name 获取子表内容

```javascript
getTableByName(tables, tableName)
```

其中

* tables: Base 中所有的表格
* tableName: 子表的 name 值

例子

```javascript
import { getTableByName } from 'dtable-utils';

const tables = window.dtableSDK.getTables();
const tableName = 'tableName';
const table = getTableByName(tables, tableName)
```
