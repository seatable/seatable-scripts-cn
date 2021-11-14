# Rows

## appendRow

添加行数据

```javascript
dtable.appendRow(table, rowData, view, { collaborators } = {});
```

其中

* table: 子表对象
* rowData: 行数据
* view: 视图对象, 可以为 null
* { collaborators } : 包含协作人列表的的对象参数

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);
const viewName = 'Default View'
const view = dtable.getViewByName(table, viewName);
const collaborators = dtable.getRelatedUsers();
const rowData = {
  '名称': '小强',
  '年龄': 28,
  '工作': '程序员'
};
dtable.appendRow(table, rowData, view, { collaborators });
```

## deleteRowById

通过 id 删除子表的行数据

```javascript
dtable.deleteRowById(table, rowId);
```

其中

* table: 子表对象
* rowId: 删除行的 id 值

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);
const viewName = 'Default View'
const view = dtable.getViewByName(table, viewName);

const rows = dtable.getViewRows(view, table);
const rowId = rows[0]._id;

dtable.deleteRowById(table, rowId);
```

## deleteRowsByIds

通过 id 列表删除子表的多行数据

```javascript
dtable.deleteRowsByIds(table, rowIds);
```

其中

* table: 子表对象
* rowIds: 删除多行数据的 id 列表

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);
const viewName = 'Default View'
const view = dtable.getViewByName(table, viewName);

const rows = dtable.getViewRows(view, table);
const rowIds = rows.map(row => row._id);

// 删除前五行数据
dtable.deleteRowsByIds(table, rowIds.slice(0, 5));
```

## modifyRow

通过 name 获取列内容

```javascript
dtable.modifyRow(table, row, updated);
```

其中

* table: 子表对象
* row: 行对象
* updated: 新的参数值对象

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);
const viewName = 'Default View'
const view = dtable.getViewByName(table, viewName);

const rows = dtable.getViewRows(view, table);
const rowId = rows[0];
const updated = {
  '年龄': 30,
  '工作': '销售'
};
dtable.modifyRow(table, row, updated);
```

## forEachRow

遍历行数据, 依据某些条件完成相应业务逻辑

```javascript
dtable.forEachRow(tableName, viewName, callback, { username, userId } = {});
```

其中

* tableName: 子表名字
* viewName: 视图名字
* callback: 回调函数, 处理自定义业务逻辑
* { username, userId }: 包含用户名字, 用户 id 的对象参数

注: username, userId: 在开发环境中可以从本地配置文件读取, 在集成环境中从 window.dtable 中读取

### 例子
```javascript
import { username, userId } from 'setting.local';

// const { username, userId } = window.dtable;

// 业务需求: 如果 行数据中的 “任务状态” 列是 “完成” 状态, 将改行中 “合格” 列设置为 “是”
const tableName = 'Table1';
const viewName = 'Default View'
dtable.forEachRow(tableName, viewName, (row) => {
  // 实现业务需求
  if (row['任务状态'] === '完成') {
    const table = dtable.getTableByName(tableName);
    const updated = {'合格': '是'};
    dtable.modifyRow(table, row, updated);
  }
}, {username, userId});

```

## getTableLinkRows

获取行数据关联其他表的所有行数据的 id 值

```javascript
dtable.getTableLinkRows(rows, table);
```

其中

* rows: 行数据
* table: 行数据所属的子表对象

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);
const viewName = 'Default View'
const view = dtable.getViewByName(table, viewName);

const rows = dtable.getViewRows(view, table);

const findLinkRows = rows.slice(0, 5);
dtable.getTableLinkRows(finLinkRows, table);
```

## getViewRows

获取视图的行数据

```javascript
dtable.getViewRows(view, table);
```

其中

* view: 视图对象
* table: 子表对象

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);
const viewName = 'Default View'
const view = dtable.getViewByName(table, viewName);

const rows = dtable.getViewRows(view, table);
```

## getGroupRows

获取视图的行数据

```javascript
dtable.getGroupRows(view, table);
```

其中

* view: 视图对象
* table: 子表对象

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);
const viewName = 'Default View'
const view = dtable.getViewByName(table, viewName);

const rows = dtable.getViewRows(view, table);
```

## getInsertedRowInitData

获取新增行的默认数据(如果表格中包含排序, 分组, 过滤等功能, 可以直接通过 api 获取新增行的默认值)

```javascript
dtable.getInsertedRowInitData(view, table, rowId);
```

其中

* view: 视图对象
* table: 子表对象
* rowId: 新增行的前一行的 id 值

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);
const viewName = 'Default View'
const view = dtable.getViewByName(table, viewName);

const rows = dtable.getViewRows(view, table);
const prevRow = rows[row.length - 1];

const defaultRowData = dtable.getInsertedRowInitData(view, table, prevRow._id);
```

## getRowsByID

通过 id 列表获取子表的相关行数据

```javascript
dtable.getRowsByID(tableId, rowIds);
```

其中

* tableId: 子表的 id 值
* rowIds: 查找行的 id 列表

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);

const rowIds = ['aaa', 'bbb', 'cccc', 'dddd'];

const rows = dtable.getRowsByID(table._id, rowIds);
```

## getRowById

通过 id 列表获取子表的相关行数据

```javascript
dtable.getRowById(table, rowId);
```

其中

* table: 子表对象
* rowId: 查找行的 id 值

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);

const rowId = 'aaaa';

const rows = dtable.getRowById(table, rowId);
```

## moveGroupRows

通过 id 列表获取子表的相关行数据

```javascript
dtable.moveGroupRows(table, targetIds, movePosition, movedRows, upperRowIds, updated, oldRows, groupbyColumns);
```

其中

* table: 子表对象
* targetIds: 移动行的目标位置行的 id 列表
* movePosition:  移动的相对位置, move_above | move_below
* movedRows: 移动的行数据列表
* upperRowIds: 所有移动行之前所在位置的前一行的 id 列表
* updated: 移动后移动行需要更新的新的属性值对象 (跨分组移动, 不同过滤条件的移动可能导致数据发生变化)
* oldRows: 移动前移动行需要更新的旧的属性值对象
* groupbyColumns: 当前视图分组的列数据

### 例子
```javascript
const tableName = 'Table1';
const table = dtable.getTableByName(tableName);
// 1. 假设: 默认行数据列表如下, 按照分组列进行分组
const rows = [
  {_id: 'aaa', '名称', '小强', '年龄': '29', '出生日期': '1992-09-09', '分组': 'a'},
  {_id: 'bbb', '名称', '小明', '年龄': '25', '出生日期': '1996-09-09', '分组': 'a'},
  {_id: 'ccc', '名称', '小红', '年龄': '24', '出生日期': '1997-09-09', '分组': 'a'},
  {_id: 'ddd', '名称', '小丽', '年龄': '22', '出生日期': '1993-09-09', '分组': 'a'},
  {_id: 'eee', '名称', '小菜', '年龄': '27', '出生日期': '1992-09-09', '分组': 'b'},
  {_id: 'fff', '名称', '小龙', '年龄': '25', '出生日期': '1990-09-09', '分组': 'b'},
  {_id: 'ggg', '名称', '小马', '年龄': '26', '出生日期': '1996-09-09', '分组': 'b'},
  {_id: 'hhh', '名称', '小正', '年龄': '27', '出生日期': '1999-09-09', '分组': 'b'},
];

// 2. 将 小明,小丽移动到小正的下面, 相关参数如下
const targetIds = ['hhh', 'hhh'];
const move_position = 'move_below';
const movedRows = [
  {_id: 'bbb', '名称', '小明', '年龄': '25', '出生日期': '1996-09-09', '分组': 'a'},
  {_id: 'ddd', '名称', '小丽', '年龄': '22', '出生日期': '1993-09-09', '分组': 'a'},
];
const upperRowIds = ['aaa', 'ccc'];
const updated = {
  'bbb': {'分组': 'b'},
  'ddd': {'分组': 'b'},
};
const oldRows = {
  'bbb': {'分组': 'a'},
  'ddd': {'分组': 'a'},
};

const groupbyColumns = [{key: '分组', name: '分组', type: 'text', ...}];

const rows = dtable.moveGroupRows(table, targetIds, movePosition, movedRows, upperRowIds, updated, oldRows, groupbyColumns);
```

