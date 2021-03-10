# Row

#### List rows

获取表格的所有行

```python
base.list_rows(table_name, view_name=None)
```

##### 例子

```python
rows = base.list_rows('Table1')
rows = base.list_rows('Table1', view_name='default')
```

#### Get row

获取表格的某一行

```python
base.get_row(table_name, row_id)
```

##### 例子

```python
row = base.get_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Append row

追加行

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

#### Insert row

插入行

```python
base.insert_row(table_name, row_data, anchor_row_id)
```

其中

* anchor_row_id: 锚定的行的 id，将会把新行插入到这行下方

##### 例子

```python
row_data = {
    "Name": "I am new Row"
}

base.insert_row('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Batch append rows

批量追加行

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

#### Update row

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

#### Delete row

删除一行

```python
base.delete_row(table_name, row_id)
```

##### 例子

```python
base.delete_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Batch delete rows

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

#### Filter rows

最新的版本请用 Queryset 提供的 filter 功能来根据条件筛选出记录。