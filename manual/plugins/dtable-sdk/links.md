# Common api

## getLinks

给指定的行添加新的关联的行数据

```javascript
window.dtableSDK.getLinks()
```

例子

```javascript
const links = window.dtableSDK.getLinks();
```


## addLink

给指定的行添加新的关联的行数据

```javascript
window.dtableSDK.addLink(linkId, tableId, otherTableId, rowId, otherRowId)
```

其中

* linkId: 链接 id
* tableId: 当前表的 id
* otherTableId: 关联表的 id
* rowId: 添加链接的行的 id
* otherRowId: 添加的行 id

例子

```javascript
const links = window.dtableSDK.getLinks();
const linkId = links[0].id;
const tableId = '0000';
const otherTableId = '1111';
const rowId = 'aaa';
const otherRowId = 'bbb';
window.dtableSDK.addLink(linkId, tableId, otherTableId, rowId, otherRowId)
```

## removeLink

从指定的行添加删除关联的行数据

```javascript
window.dtableSDK.removeLink(linkId, tableId, otherTableId, rowId, otherRowId)
```

其中

* linkId: 链接 id
* tableId: 当前表的 id
* otherTableId: 关联表的 id
* rowId: 删除链接的行的 id
* otherRowId: 删除的行 id

例子

```javascript
const links = window.dtableSDK.getLinks();
const linkId = links[0].id;
const tableId = '0000';
const otherTableId = '1111';
const rowId = 'aaa';
const otherRowId = 'bbb';
window.dtableSDK.removeLink(linkId, tableId, otherTableId, rowId, otherRowId);
```


