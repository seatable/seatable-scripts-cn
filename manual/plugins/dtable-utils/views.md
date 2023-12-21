# Views

## getNonArchiveViews

获取 table 中的非私有且非归档视图

```javascript
getNonArchiveViews(views);
```

其中

* views: 所有子表的视图

例子

```javascript
import { getTableById, getNonArchiveViews } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const views = getNonArchiveViews(table.views);
```

## getViewById

通过 id 获取视图内容

```javascript
getViewById(views, viewId);
```

其中

* views: 所有子表的视图
* viewId: 获取视图的id

例子

```javascript
import { getTableById, getViewById } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const viewId = '0000';
const view = getViewById(table.views, viewId);
```

## getViewByName

通过 name 获取视图内容

```javascript
getViewByName(views, viewName);
```

其中

* views: 所有子表的视图
* viewName: 获取视图的名字

例子

```javascript
import { getTableById, getViewByName } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const viewId = '0000';
const viewName = 'viewName';
const view = getViewByName(table.views, viewName);
```

## isDefaultView

判断是否为默认视图(不包含分组, 过滤, 排序等条件)

```javascript
isDefaultView(view, columns);
```

其中

* view: 视图对象
* columns: 子表中所有的列内容

例子

```javascript
import { getTableById, getViewById, isDefaultView } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const viewId = '0000';
const view = getViewById(table.views, viewId);


const columns = window.dtableSDK.getColumns(table); // const columns = view.columns
const _isDefaultView = isDefaultView(view, columns);
```

## isGroupView

判断是否为包含分组的视图(包含分组条件)

```javascript
isGroupView(view, columns);
```

其中

* view: 视图对象
* columns: 子表中所有的列内容

例子

```javascript
import { getTableById, getViewById, isGroupView } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const viewId = '0000';
const view = getViewById(table.views, viewId);


const columns = window.dtableSDK.getColumns(table); // const columns = view.columns
const _isGroupView = isGroupView(view, columns);
```

## isFilterView

判断是否为过滤视图(包含过滤条件)

```javascript
isFilterView(view, columns);
```

其中

* view: 视图对象
* columns: 子表中所有的列内容

例子

```javascript
import { getTableById, getViewById, isFilterView } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = '0000';
const table = getTableById(tables, tableId);

const viewId = '0000';
const view = getViewById(table.views, viewId);


const columns = window.dtableSDK.getColumns(table); // const columns = view.columns
const _isFilterView = isFilterView(view, columns);
```
