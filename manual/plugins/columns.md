# Columns

## getColumns

获取子表所有的列内容

```javascript
dtable.getColumns(table);
```

其中

* table: 子表对象

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const columns = dtable.getColumns(table);
```

## getShownColumns

获取视图所有显示的列内容(不包含隐藏列)

```javascript
dtable.getShownColumns(table, view);
```

其中

* table: 子表对象
* view: 子表中的视图对象

### 例子
```javascript
const tableId = '0000';
const viewId = '0000';
const table = dtable.getTableById(tableId);
const view = dtable.getViewById(table, viewId);
const shownColumns = dtable.getShownColumns(table, view);
```

## getColumnsByType

获取子表中所有类型一样的列内容

```javascript
dtable.getColumnsByType(table, type);
```

其中

* table: 子表对象
* type: 获取列的类型

### 例子
```javascript
import { CELL_TYPE } from 'dtable-sdk';

const tableId = '0000';
const table = dtable.getTableById(tableId);
const columnType = CELL_TYPE.TEXT;
const sameTypeColumns = dtable.getColumnsByType(table, columnType);
```

## getColumnByName

通过 name 获取列内容

```javascript
dtable.getColumnByName(table, columnName);
```

其中

* table: 子表对象
* columnName: 获取列的名字

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const columnName = 'columnName';
const column = dtable.getColumnByName(table, columnName);
```

## getColumnByKey

通过 key 获取列内容

```javascript
dtable.getColumnByKey(table, columnKey);
```

其中

* table: 子表对象
* columnKey: 获取列的 key 值

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const columnKey = '0000';
const column = dtable.getColumnByKey(table, columnKey);
```

## modifyColumnData

更新列的 data 属性

```javascript
dtable.modifyColumnData(table, columnName, columnData);
```

其中

* table: 子表对象
* columnName: 更新列的 name 值
* columnData: 更新列的新 data 属性

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const columnName = 'dateColumn';
const data = {
  format: 'YYYY-MM-DD'
};
dtable.modifyColumnData(table, columnName, data);
```
