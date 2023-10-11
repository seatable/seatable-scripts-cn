# Column

#### List columns

列出表/视图所有列

```python
base.list_columns(table_name, view_name=None)
```

其中

* table_name: 子表名称或 id

##### 例子

```python
base.list_columns('Table1')
base.list_columns('Table1', view_name='default')
```

#### Insert column

插入/追加列

```python
base.insert_column(table_name, column_name, column_type, column_key=None, column_data=None)
```

其中

* table_name: 子表名称或 id

* column_key：要插入的位置的前一列的 key，如若省略则默认追加为最后一列
* column_type：请参考 [constants](../constants)
* column_data: 一个列的 config 信息，创建链接列时需要指定， 其他类型选择性制定

##### 例子

```python
from seatable_api.constants import ColumnTypes
base.insert_column('Table1', 'python-api', ColumnTypes.TEXT)
base.insert_column('Table1', 'python-api', ColumnTypes.TEXT, '0000')
base.insert_column('Table1', 'Link1', ColumnTypes.LINK, column_data={
        'table':'Table1',
        'other_table':'Test_User'
    })
```

#### Rename column

重命名列

```python
base.rename_column(table_name, column_key, new_column_name)
```

其中

* table_name: 子表名称或 id

##### 例子

```python
base.rename_column('Table1', 'kSiR', 'new-python-api')
```

#### Resize column

设置列宽

```python
base.resize_column(table_name, column_key, new_column_width)
```

其中

* table_name: 子表名称或 id

##### 例子

列的默认宽度为200，如果需要调整列宽比如调整为500，则

```python
base.resize('Table1', 'asFV', 500)
```

#### Freeze column

冻结列

```python
base.freeze_column(table_name, column_key, frozen)
```

其中

* table_name: 子表名称或 id

* frozon: True/False

##### 例子

```python
base.freeze_column('Table1', '0000', True)
```

#### Move column

```python
base.move_column(table_name, column_key, target_column_key)
```

其中

* table_name: 子表名称或 id

* column_key：要移动的列的 key

* target_column_key： 锚定列的 key，被移动的列将会被移动到该列右边

##### 例子

```python
base.move_column('Table1', 'loPx', '0000')
```

此例中，`loPx`列将会被移动到`0000`列的右边

#### Modify column type

转换列类型

```python
base.modify_column_type(table_name, column_key, new_column_type)
```

其中

* table_name: 子表名称或 id

* column_type：请参考 [constants](../constants)

##### 例子

```python
from seatable_api.constants import ColumnTypes

base.modify_column_type('Table1', 'nePI', ColumnTypes.NUMBER)
```

#### Add column options

单选，多选列专用，添加选项

```python
add_column_options(table_name, column, options)
```

其中

* table_name: 子表名称或 id

##### 例子

```python
base.add_column_options('Table1', 'My choices', [
        {"name": "ddd", "color": "#aaa", "textColor": "#000000"},
        {"name": "eee", "color": "#aaa", "textColor": "#000000"},
        {"name": "fff", "color": "#aaa", "textColor": "#000000"},
])
```

#### Add column cascade settings

单选列专用，添加单选选项的父子及联关系，达到子列的单选选项条目根据父列的选项而定的效果

```python
add_column_cascade_settings(table_name, child_column, parent_column, cascade_settings)
```

其中

* table_name: 子表名称或 id

* child_column: 单选子列的名称
* parent_column: 单选父列的名称
* cascade_settings: 及联关系设置数据

##### 例子

```python
base.add_column_cascade_settings("Table1", "single-op-col-c", "single-op-col", {
  "aaa": ["aaa-1", "aaa-2"], # 如果父列选择 “aaa”， 子列只有 “aaa-1” 和 “aaa-2” 可选 
  "bbb": ["bbb-1", "bbb-2"],
  "ccc": ["ccc-1", "ccc-2"]
})
```

#### Delete column

删除列

```python
base.delete_column(table_name, column_key)
```

其中

* table_name: 子表名称或 id

##### 例子

```python
base.delete_column('Table1', 'bsKL')
```

