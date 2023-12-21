# Columns

## getColumns

获取子表所有的列内容

```javascript
window.dtableSDK.getColumns(table);
```

其中

* table: 子表对象

### 例子
```javascript
import { getTableById } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)

const columns = window.dtableSDK.getColumns(table); // const columns = table.columns;
```


## modifyColumnData

更新列的 data 属性

```javascript
window.dtableSDK.modifyColumnData(table, columnName, columnData);
```

其中

* table: 子表对象
* columnName: 更新列的 name 值
* columnData: 更新列的新 data 属性

### 例子
```javascript
import { getTableById } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)

const columnName = 'dateColumn';
const data = {
  format: 'YYYY-MM-DD'
};
window.dtableSDK.modifyColumnData(table, columnName, data);
```
