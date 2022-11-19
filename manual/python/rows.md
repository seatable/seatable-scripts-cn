# Row

#### List rows

获取表格的所有行

```python
base.list_rows(table_name, view_name=None, order_by=None, desc=False, start=None, limit=None)
```

其中

* table_name: 子表名称或 ID

* order_by: 根据某列名进行排序
* desc： 是否降序，默认为升序
* start: 索引的起始位置， 行号
* limit: 数据的显示数量

##### 例子

```python
rows = base.list_rows('Table1')
rows = base.list_rows('Table1', view_name='default', order_by='年龄', desc=True, start=5, limit=20)
```

#### Get row

获取表格的某一行

```python
base.get_row(table_name, row_id)
```

其中

* table_name: 子表名称或 ID

##### 例子

```python
row = base.get_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Append row

追加行

```python
base.append_row(table_name, row_data)
```

其中

* table_name: 子表名称或 ID

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

* table_name: 子表名称或 ID

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

其中

* table_name: 子表名称或 ID

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

其中

* table_name: 子表名称或 ID

##### 例子

```python
row_data = {
    "dcXS": "123"
}
base.update_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
```

#### Batch update rows

批量更新行

```python
batch_update_rows(table_name, rows_data)
```

其中

* table_name: 子表名称或 ID

##### 例子

```python
updates_data = [
        {
            "row_id": "fMmCFyoxT4GN5Y2Powbl0Q",
            "row": {
                "Name": "Ranjiwei",
                "age": "36"
            }
        },
        {
            "row_id": "cF5JTE99Tae-VVx0BGT-3A",
            "row": {
                "Name": "Huitailang",
                "age": "33"
            }
        },
        {
            "row_id": "WP-8rb5PSUaM-tZRmTOCPA",
            "row": {
                "Name": "Yufeng",
                "age": "22"
            }
        }
    ]
base.batch_update_rows('Table1', rows_data=updates_data)
```

#### Delete row

删除一行

```python
base.delete_row(table_name, row_id)
```

其中

* table_name: 子表名称或 ID

##### 例子

```python
base.delete_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Batch delete rows

批量删除行

```python
base.batch_delete_rows(table_name, row_ids)
```

其中

* table_name: 子表名称或 ID

##### 例子

```python
del_rows = rows[:3]
row_ids = [row['_id'] for row in del_rows]
base.batch_delete_rows('Table1', row_ids)
```

#### Filter rows

最新的版本请用 SQL Query 函数提供的查询功能。
