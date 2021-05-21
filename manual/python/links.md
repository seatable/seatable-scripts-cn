# Links


#### Add link

添加链接，链接其他表记录

```python
base.add_link(link_id, table_name, other_table_name, row_id, other_row_id)
```

其中

* link_id: 链接列data属性下的 link_id
* table_name: 链接表的名字
* other_table_name: 被链接表的名字
* row_id: 链接行 id
* other_row_id: 被链接行的 id

##### 例子

```python
base.add_link('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```

#### Update link

更新链接信息

```
update_link(self, link_id, table_id, other_table_id, row_id, other_rows_ids)
```

其中

* link_id: 链接列data属性下的 link_id
* table_id: 链接表的id
* other_table_id: 被链接表的id
* row_id: 链接行 id
* other_rows_ids: 被链接行的id列表

##### 例子

```python
base.update_link(
        link_id='r4IJ',
        table_id='0000',
        other_table_id='kFoO',
        row_id='BXhEm9ucTNu3FjupIk7Xug',
        other_rows_ids=[
          'exkb56fAT66j8R0w6wD9Qg',
          'DjHjwmlRRB6WgU9uPnrWeA'
        ]
    )
```

#### Batch update links

批量更新链接信息

```
batch_update_links(self, links)
```

##### 例子

```python
links = [
        {
            "row_id":'NK6ImdjPTMy0baWIg5sfmA',
            "link_id":'r4IJ',
            "table_id":'0000',
            "other_table_id":'kFoO',
            "other_rows_ids":['exkb56fAT66j8R0w6wD9Qg',
                              'DjHjwmlRRB6WgU9uPnrWeA']
        },
        {
            "row_id": 'chyxfYc-S8SHQmaJ2i20Vg',
            "link_id": 'r4IJ',
            "table_id": '0000',
            "other_table_id": 'kFoO',
            "other_rows_ids": ['Ufrm3ZLmSiiqJcKvlPdsGw',
                               'DjHjwmlRRB6WgU9uPnrWeA']
        },...
]

base.batch_update_links(links)
```

#### Remove link

移除某个链接

```python
base.remove_link(link_id, table_name, other_table_name, row_id, other_row_id)
```

##### 例子

```python
base.remove_link('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```

#### Get link id

通过列名来获取链接的id

```python
base.get_column_link_id(table_name, column_name, view_name=None)
```

##### 例子

```python
base.get_column_link_id('Table1', '记录') # 返回链接的id，如‘aHL2’
```

