# Links


#### add link

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

#### remove link

添加链接，链接其他表记录

```python
base.remove_link(link_id, table_name, other_table_name, row_id, other_row_id)
```

##### 例子

```python
base.remove_link('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```
