# Views

## addView

添加视图

```javascript
window.dtableSDK.addView(tableName, viewName);
```

其中

* tableName: 子表名字
* viewName: 添加视图的名字

例子

```javascript
window.dtableSDK.addView('tableName', 'viewName');
```

## deleteView

删除视图

```javascript
window.dtableSDK.deleteView(tableName, viewName);
```

其中

* tableName: 子表名字
* viewName: 删除视图的名字

例子

```javascript
window.dtableSDK.deleteView('TableName', ViewName);
```

## renameView

修改视图名字

```javascript
window.dtableSDK.renameView(tableName, oldViewName, newViewName);
```

其中

* tableName: 子表的名字
* oldViewName: 视图的旧名字
* newViewName: 视图的新名字

例子

```javascript
window.dtableSDK.renameView('tableName', 'oldViewName', 'newViewName');
```

## getViews

获取 table 中的非私有视图

```javascript
window.dtableSDK.getViews(table);
```

其中

* table: 子表对象

例子

```javascript
import { getTableById } from 'dtable-utils';

const tables = window.dtableSDK.getTables();
const tableId = '0000';
const table = getTableById(tables, tableId);
const views = window.dtableSDK.getViews(table); // const views = table.views
```

## getActiveView

获取当前 base 正在访问的视图

```javascript
window.dtableSDK.getActiveView();
```

例子

```javascript
const view = window.dtableSDK.getActiveView();
```
