# Views

## addView

添加视图

```javascript
dtable.addView(tableName, viewName);
```

其中

* tableName: 子表名字
* viewName: 添加视图的名字

### 例子
```javascript
dtable.addView('tableName', 'viewName');
```

## deleteView

删除视图

```javascript
dtable.deleteView(tableName, viewName);
```

其中

* tableName: 子表名字
* viewName: 删除视图的名字

### 例子
```javascript
dtable.deleteView('TableName', ViewName);
```

## renameView

修改子表名字

```javascript
dtable.renameView(tableName, oldViewName, newViewName);
```

其中

* tableName: 子表的名字
* oldViewName: 更视图的旧名字
* newViewName: 更视图的新名字

### 例子
```javascript
dtable.renameView('tableName', 'oldViewName', 'newViewName');
```

## getViews

获取 table 中的所有视图

```javascript
dtable.getViews(table);
```

其中

* table: 子表对象

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const views = dtable.getViews(table);
```

## getNonArchiveViews

获取 table 中的所有非归档视图

```javascript
dtable.getNonArchiveViews(table);
```

其中

* table: 子表对象

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const views = dtable.getNonArchiveViews(table);
```

## getActiveView

获取当前 base 正在访问的视图

```javascript
dtable.getActiveView();
```

### 例子
```javascript
const view = dtable.getActiveView();
```

## getViewByName

通过 name 获取视图内容

```javascript
dtable.getViewByName(table, viewName);
```

其中

* table: 子表对象
* viewName: 获取视图的名字

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const viewName = 'viewName';
const view = dtable.getViewByName(table, viewName);
```

## getViewById

通过 id 获取视图内容

```javascript
dtable.getViewById(table, viewId);
```

其中

* table: 子表对象
* viewId: 获取视图的id

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const viewId = '0000';
const view = dtable.getViewById(table, viewId);
```

## isDefaultView

判断是否为默认视图(不包含分组, 过滤, 排序等条件)

```javascript
dtable.isDefaultView(view, columns);
```

其中

* view: 视图对象
* columns: 子表中所有的列内容

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const viewId = '0000';
const view = dtable.getViewById(table, viewId);
const columns = dtable.getColumns(table);
const isDefaultView = dtable.isDefaultView(view, columns);
```

## isGroupView

判断是否为包含分组的视图(包含分组条件)

```javascript
dtable.isGroupView(view, columns);
```

其中

* view: 视图对象
* columns: 子表中所有的列内容

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const viewId = '0000';
const view = dtable.getViewById(table, viewId);
const columns = dtable.getColumns(table);
const isGroupView = dtable.isGroupView(view, columns);
```

## isFilterView

判断是否为过滤视图(包含过滤条件)

```javascript
dtable.isFilterView(view, columns);
```

其中

* view: 视图对象
* columns: 子表中所有的列内容

### 例子
```javascript
const tableId = '0000';
const table = dtable.getTableById(tableId);
const viewId = '0000';
const view = dtable.getViewById(table, viewId);
const columns = dtable.getColumns(table);
const isFilterView = dtable.isFilterView(view, columns);
```
