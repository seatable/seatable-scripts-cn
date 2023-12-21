# Tables

## addTable

添加子表

```javascript
window.dtableSDK.addTable(tableName);
```

其中

* tableName: 添加子表的名称

例子

```javascript
window.dtableSDK.addTable('newTable');
```

## deleteTable

删除子表

```javascript
window.dtableSDK.deleteTable(tableName);
```

其中

* tableName: 删除子表的名称

例子

```javascript
window.dtableSDK.deleteTable('newTable');
```

## renameTable

修改子表名字

```javascript
window.dtableSDK.renameTable(oldTableName, newTableName);
```

其中

* oldTableName: 更新子表的旧名字
* newTableName: 更新子表的新名字

例子

```javascript
window.dtableSDK.renameTable('oldTableName', 'newTableName');
```

## getTables

获取 base 中所有的子表

```javascript
window.dtableSDK.getTables();
```

例子

```javascript
const tables = window.dtableSDK.getTables();
```

## getActiveTable

获取当前 base 正在访问的子表

```javascript
window.dtableSDK.getActiveTable();
```

例子

```javascript
const table = window.dtableSDK.getActiveTable();
```

## importDataIntoNewTable

向 base 中添加新的子表,并包含默认数据

```javascript
window.dtableSDK.importDataIntoNewTable(tableName, columns, rows);
```

其中

* tableName: 新表的名字
* columns: 新表的列数据
* rows: 新表的行数据

例子

```javascript
const tableName = 'tableName';
const columns = [
  {
    key: '0000',
    type: 'text',
    name: 'column1',
    width: 200,
  },
  {
    key: '1111',
    type: 'date',
    name: 'column2',
    width: 300,
    data: {
      format: 'YYYY-MM-DD'
    }
  }
];
const rows = [
  {'0000': '小强', '1111': '1993-03-03'},
  {'0000': '小明', '1111': '1993-04-04'},
  {'0000': '小红', '1111': '1994-04-05'},
];
window.dtableSDK.importDataIntoNewTable(tableName, columns, rows);
```
