# Column

#### List columns

列出表/视图所有行

```python
base.list_columns(table_name, view_name=None)
```

##### 例子

```python
base.list_columns('Table1')
base.list_columns('Table1', view_name='default')
```

#### Insert column

插入/追加列

```python
base.insert_column(table_name, column_name, column_type, column_key=None)
```

其中

* column_key：要插入的位置的前一列的 key 或者列名，如若省略则默认追加为最后一列

* column_type：请参考 [constants](../constants)

##### 例子

```python
from seatable_api.constants import ColumnTypes
base.insert_column('Table1', 'python-api', ColumnTypes.TEXT)
base.insert_column('Table1', 'python-api', ColumnTypes.TEXT, '0000')
base.insert_column('Table1', 'python-api', ColumnTypes.TEXT, '体重')
```

#### Rename column

重命名列

```python
base.rename_column(table_name, column_key, new_column_name)
```

##### 例子

```python
base.rename_column('Table1', 'kSiR', 'new-python-api')
base.rename_column('Table1', 'python-api', 'new-python-api')
```

#### Resize column

设置列宽

```python
base.resize_column(table_name, column_key, new_column_width)
```

##### 例子

列的默认宽度为200，如果需要调整列宽比如调整为500，则

```python
base.resize('Table1', 'asFV', 500)
base.resize('Table1', '部门', 300)
```

#### Freeze column

冻结列

```python
base.freeze_column(table_name, column_key, frozen)
```

frozon: True/False

##### 例子

```python
base.freeze_column('Table1', '0000', True)
base.freeze_column('Table1', '年龄', True)
```

#### Move column

```python
base.move_column(table_name, column_key, target_column_key)
```

其中

* column_key：要移动的列的 key 或列名

* target_column_key： 锚定列的 key 或列名，被移动的列将会被移动到该列右边

##### 例子

```python
base.move_column('Table1', 'loPx', '0000')
base.move_column('Table1', '姓名', '兴趣爱好')
```

此例中，`loPx`列将会被移动到`0000`列的右边

#### Modify column type

转换列类型

```python
base.modify_column_type(table_name, column_key, new_column_type)
```

其中

* column_type：请参考 [constants](../constants)

##### 例子

```python
from seatable_api.constants import ColumnTypes

base.modify_column_type('Table1', 'nePI', ColumnTypes.NUMBER)
base.modify_column_type('Table1', '详情', ColumnTypes.TEXT)
```

#### Delete column

删除列

```python
base.delete_column(table_name, column_key)
```

##### 例子

```python
base.delete_column('Table1', 'bsKL')
base.delete_column('Table1', '性别')
```

