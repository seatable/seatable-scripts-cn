# Row

`seatable-api` 模块提供了一系列操作 base 中行的方法

大多数操作方法中参数使用到的名称以及数据结构描述如下：

* table_name: 子表名称或 id， 字符串
* row_id: 行的 id， 字符串
* row_data: 行数据， 字典
* rows_data: 多行数据， 包含字典的列表

##### 例子

```python
row_data = {
    "Name": "Ron",
  	"Age": 20
}

rows_data = [{
                'Name': 'Tom',
                'Age': 18
            }, {
                'Name': '小明',
                'Age': 33
            }, ....
]
```

#### List rows

获取表格的行

```python
base.list_rows(table_name, view_name=None, order_by=None, desc=False, start=None, limit=None)
```

其中

* table_name: 子表名称或 id
* view_name: 视图名称或 id， 如果设定， 会返回满足视图设定条件的行数据
* order_by: 按照某列排序的列名
* desc:  是否是降序， 默认为 False
* start: 索引的起始位置， 行号
* limit: 数据的显示数量， 最大返回 1000 行 (即使设定值超过 1000 行)

使用 [SQL 查询](../sql/sql.md) 可以设定更加灵活的过滤条件检索到更多的行.

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

##### 例子

```python
row = base.get_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Append row

追加行

```python
base.append_row(table_name, row_data, apply_default=False)
```

其中

* apply_default:  是否使用表格列中设置的默认值，如果设置为 True，那么这一列在 row_data 中没有指定的情况下，会使用默认值。默认为 False。

例子

```python
row_data = {
    "Name": "I am new Row"
}

base.append_row('Table1', row_data)
```

#### Insert row (deprecated)

插入行（seatable-api 2.7.0 版本以后将不再支持该方法）

```python
base.insert_row(table_name, row_data, anchor_row_id, apply_default=False)
```

* anchor_row_id: 锚定的行的 id，将会把新行插入到这行下方


##### 例子

```python
row_data = {
    "Name": "I am new Row"
}

base.insert_row('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw', apply_default=True)
```

#### Batch append rows

批量追加行

```python
base.batch_append_rows(table_name, rows_data, apply_default=False)
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

#### Batch update rows

批量更新行

```python
batch_update_rows(table_name, rows_data)
```

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
