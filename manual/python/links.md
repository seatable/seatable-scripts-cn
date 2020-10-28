# Links

本文档将展示通过Base对象如何操作链接

如果您对Base对象还未了解，请参考

* [Base](base.md)


#### add link

添加链接，链接其他表记录

```python
# link_id: 链接列data属性下的link_id
# table_name: 链接表的名字
# other_table_name: 被链接表的名字
# row_id: 链接的行id
# other_row_id: 被链接行的id
base.add_link(link_id, table_name, other_table_name, row_id, other_row_id)
```

##### 例子

```python
base.add_link('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```

#### remove link

添加链接，链接其他表记录

```python
# link_id: 链接列data属性下的link_id
# table_name: 链接表的名字
# other_table_name: 被链接表的名字
# row_id: 链接的行id
# other_row_id: 被链接行的id
base.remove_link(link_id, table_name, other_table_name, row_id, other_row_id)
```

##### 例子

```python
base.remove_link('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```
