# Links

#### Get linked records

获取被链接的行的信息。可以一次查询多个行的被链接行的信息。

```javascript
base.getLinkedRecords(table_id, link_column_key, rows)
```

其中

* table_id: 子表的 id
* link_column_key: 链接列的 key (非 link_id )
* rows: 需要查找链接信息的行的列表，每一列表项包含三个参数 row_id, offset (查找的偏移量, 默认为0)， limit (查找的数量， 默认为10)

##### 例子

```javascript
base.getLinkedRecords('0000', '89o4', [
  {'row_id': 'FzNqJxVUT8KrRjewBkPp8Q', 'limit': 2, 'offset': 0},
  {'row_id': 'Jmnrkn6TQdyRg1KmOM4zZg', 'limit': 20}
])

// 返回的数据结构, 包含被链接的行的 ID 和显示值。每个行所连接的行，按照被链接的行的创建时间顺序以数组形式返回。
{
  'FzNqJxVUT8KrRjewBkPp8Q': [
    {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'},                            
    {'row_id': 'OA6x7CYoRuyc2pT52Znfmw', 'display_value': '3'},
    ...
  ],
  'Jmnrkn6TQdyRg1KmOM4zZg': [
    {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'},     
    {'row_id': 'OA6x7CYoRuyc2pT52Znfmw', 'display_value': '3'},
    ...
  ]
}
```

#### Add link

添加链接，链接其他表记录

```javascript
base.addLink(link_id, table_name, other_table_name, row_id, other_row_id)
```

其中

* link_id: 链接列 data 属性下的 link_id (你可以获取 base 的 metadata，找到对应的列，然后找一下 data 字段下的 link_id 字段)
* table_name: 链接表的名字
* other_table_name: 被链接表的名字
* row_id: 链接行 id
* other_row_id: 被链接行的 id

##### 例子

```javascript
await base.addLink('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```

#### Update link

更新链接信息

```javascript
base.updateLink(self, link_id, table_name, other_table_name, row_id, other_rows_ids)
```

其中

* link_id: 链接列 data 属性下的 link_id 
* table_name: 链接表的 名称
* other_table_name: 被链接表的 名称
* row_id: 链接行 id
* other_rows_ids: 被链接行的 id 列表


##### 例子

```javascript
await base.updateLink(
        link_id='r4IJ',
        table_name='Table1',
        other_table_name='Table2',
        row_id='BXhEm9ucTNu3FjupIk7Xug',
        other_rows_ids=[
          'exkb56fAT66j8R0w6wD9Qg',
          'DjHjwmlRRB6WgU9uPnrWeA'
        ]
    )
```

#### Batch update links

批量更新链接信息

```javascript
base.batchUpdateLinks(link_id, table_name, other_table_name, row_id_list, other_rows_ids_map)
```

##### 例子

```javascript
link_id = "WaW5"
table_name ="Table1"
other_table_id = "Table2"
row_id_list = ["fRLglslWQYSGmkU7o6KyHw","eSQe9OpPQxih8A9zPXdMVA","FseN8ygVTzq1CHDqI4NjjQ"]
other_rows_ids_map = {
    	"FseN8ygVTzq1CHDqI4NjjQ":["OcCE8aX8T7a4dvJr-qNh3g","JckTyhN0TeS8yvH8D3EN7g"],
    	"eSQe9OpPQxih8A9zPXdMVA":["cWHbzQiTR8uHHzH_gVSKIg","X56gE7BrRF-i61YlE4oTcw"],
    	"fRLglslWQYSGmkU7o6KyHw":["MdfUQiWcTL--uMlrGtqqgw","E7Sh3FboSPmfBlDsrj_Fhg","UcZ7w9wDT-uVq4Ohtwgy9w"]
}

await base.batchUpdateLinks(link_id, table_id, other_table_id, row_id_list, other_rows_ids_map)
```

#### Remove link

移除某个链接

```javascript
base.removeLink(link_id, table_name, other_table_name, row_id, other_row_id)
```

##### 例子

```javascript
await base.removeLink('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```

#### Get link id

通过列名来获取链接的id

```javascript
base.getColumnLinkId(table_name, column_name)
```

##### 例子

```javascript
const linkId = await base.getColumnLinkId('TableLink', '记录') # 返回链接的id，如‘aHL2’
```
