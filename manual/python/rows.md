# Row

本文档将展示通过Base对象如何对行进行操作

如果您对Base对象还未了解，请参考

* [Base](base.md)

#### list rows

获取表格的所有行

```python
base.list_rows(table_name, view_name=None)
```

##### 例子

```python
rows = base.list_rows('Table1')
rows = base.list_rows('Table1', view_name='default')
```

#### append row

追加表格

```python
base.append_row(table_name, row_data)
```

##### 例子

```python
row_data = {
    "Name": "I am new Row"
}

base.append_row('Table1', row_data)
```

#### insert row

插入表格

```python
base.insert_row(table_name, row_data, anchor_row_id)
# anchor_row_id为锚定的行的id，将会把新行插入到这行下方
```

##### 例子

```python
row_data = {
    "Name": "I am new Row"
}

base.insert_row('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw')
```

#### batch append rows

批量追加到表格

```python
base.batch_append_rows(table_name, rows_data)
```

##### 例子

```python
rows_data = [{
                'Name': 'test batch',
                'content': 'Yes'
            }, {
                'Name': 'test batch',
                'content': 'Yes'
            }, {
                'Name': 'test batch',
                'content': 'Yes'
            }]
base.batch_append_rows('Table6', rows_data)
```

#### update row

更新一行

```python
base.update_row(table_name, row_id, row_data)
```

##### 例子

```python
row_data = {
    "dcXS": "123"
}
base.update_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
```

#### delete row

删除一行

```python
base.delete_row(table_name, row_id)
```

##### 例子

```python
base.delete_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### batch delete rows

批量删除行

```python
base.batch_delete_rows(table_name, row_ids)
```

##### 例子

```python
del_rows = rows[:3]
row_ids = [row['_id'] for row in del_rows]
base.batch_delete_rows('Table1', row_ids)
```

#### filter rows

过滤行

```python
base.filter_rows(table_name, filters, view_name=None, filter_conjunction='And')
```

##### 例子

```python
filters = [{
    "column_name":"姓名",  
    "filter_predicate":"contains", # 有“contains“和”is“两种，其中”contains“是模糊查找，”is“是精确查找过滤
    "filter_term":"a"
}],
base.filter_rows('Table1', filters=filters) # 筛选出姓名中包含“a”的row
```
