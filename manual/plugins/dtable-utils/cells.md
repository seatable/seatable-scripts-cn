# Cell

## getLinkCellValue

获取子表行数据关联其他表格的行数据的 id 列表

```javascript
getLinkCellValue(links, linkId, tableId, otherTableId, rowId)
```

其中

* links: 当前 base 中的 links 值
* linkId: link 列对应的 link_id 值
* tableId: 当前表格的 id 值
* otherTableId: 关联表格的 id 值
* rowId: 当前表格中行的 id 值

例子

```javascript
import { getTableById, getTableColumnByName, getLinkCellValue } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)


const rows = table.rows;
const row = rows[0];

const columnName = 'linkColumn';
const column = getTableColumnByName(table, columnName);

const { link_id, table_id, other_table_id, display_column_key } = linkColumn.data;
const linkedTableId = table._id === table_id ? other_table_id : table_id;

const links = window.dtableSDK.getLinks();
const linkedRowIds = getLinkCellValue(links, link_id, table._id, linkedTableId, row._id);
```

## getNumberDisplayString

获取 number 列的字符串显示(按照不同的format返回用户数据)

```javascript
getNumberDisplayString(value, columnData)
```

其中

* value: number 类型列对应的 value 值
* columnData: number 类型列 对应的 column 的 data 配置属性

例子

```javascript
import { getTableById, getTableColumnByKey, getNumberDisplayString } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)

const columnKey = '0000';
const column = getTableColumnByKey(table, columnKey);

const value = 190203;
const name = getNumberDisplayString(value, column.data);
```

## getGeolocationDisplayString

获取 geolocation 列的字符串显示(按照不同的配置参数返回用户数据)

```javascript
getGeolocationDisplayString(value, columnData)
```

其中

* value: geolocation 类型列对应的 value 值
* columnData: geolocation 类型列 对应的 column 的 data 配置属性

例子

```javascript
import { getTableById, getTableColumnByKey, getGeolocationDisplayString } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)

const columnKey = '0000';
const column = getTableColumnByKey(table, columnKey);

const value = {city: "安庆市", detail: "nide" ,district: "迎江区", province: "安徽省"};
const name = getGeolocationDisplayString(value, column.data);
```

## getDurationDisplayString

获取 duration 列的字符串显示(按照不同的配置参数返回用户数据)

```javascript
getDurationDisplayString(value, columnData)
```

其中

* value: duration 类型列对应的 value 值
* columnData: duration 类型列 对应的 column 的 data 配置属性

例子

```javascript
import { getTableById, getTableColumnByKey, getDurationDisplayString } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)

const columnKey = '0000';
const column = getTableColumnByKey(table, columnKey);

const value = '12:30';
const name = getDurationDisplayString(value, column.data);
```

## getDateDisplayString

获取 date 列的字符串显示(按照不同的配置参数返回用户数据)

```javascript
getDateDisplayString(value, columnData)
```

其中

* value: date 类型列对应的 value 值
* format: date 的类型

例子

```javascript
import { getTableById, getTableColumnByKey, getDateDisplayString } from 'dtable-utils';

const tables = window.dtableSDK.getTables();

const tableId = 'tableId';
const table = getTableById(tables, tableId)

const columnKey = '0000';
const column = getTableColumnByKey(table, columnKey);

const value = 'YYYY-MM-DD';
const { format } = column.data;
const name = getDateDisplayString(value, format);
```