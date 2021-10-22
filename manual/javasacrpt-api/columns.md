# Column

#### List columns

列出表/视图所有行

```javascript
base.listColumns(table_name, view_name='')
```

##### 例子

```javascript
const columns1 = await base.listColumns('Table1')
const columns2 = await base.listColumns('Table1', view_name='default')
```

#### Insert column

插入/追加列

```javascript
base.insertColumn(table_name, column_name, column_type, column_key='', column_data='')
```

其中

* column_key：要插入的位置的前一列的 key，如若省略则默认追加为最后一列
* column_type：请参考 [constants](../constants)
* column_data: 一个列的 config 信息，创建链接列时需要指定， 其他类型选择性制定

##### 例子

```javascript
import { ColumnTypes } from 'seatable-api';

await base.insertColumn('Table1', 'seatable-api', ColumnTypes.TEXT)
await base.insertColumn('Table1', 'seatable-api', ColumnTypes.TEXT, '0000')
await base.insertColumn('Table1', 'Link1', ColumnTypes.LINK, column_data={
        'table':'Table1',
        'other_table':'Test_User'
    })
```

#### Rename column

重命名列

```javascript
base.renameColumn(table_name, column_key, new_column_name)
```

##### 例子

```javascript
await base.renameColumn('Table1', 'kSiR', 'new-seatable-api')
```

#### Resize column

设置列宽

```javascript
base.resizeColumn(table_name, column_key, new_column_width)
```

##### 例子

列的默认宽度为200，如果需要调整列宽比如调整为500，则

```javascript
await base.resizeColumn('Table1', 'asFV', 500)
```

#### Freeze column

冻结列

```javascript
base.freezeColumn(table_name, column_key, frozen)
```

frozen: true/false

##### 例子

```javascript
await base.freezeColumn('Table1', '0000', true)
```

#### Move column

```javascript
base.moveColumn(table_name, column_key, target_column_key)
```

其中

* column_key：要移动的列的 key

* target_column_key： 锚定列的 key，被移动的列将会被移动到该列右边

##### 例子

```javascript
await base.moveColumn('Table1', 'loPx', '0000')
```

此例中，`loPx`列将会被移动到`0000`列的右边

#### Modify column type

转换列类型

```javascript
base.modifyColumnType(table_name, column_key, new_column_type)
```

其中

* column_type：请参考 [constants](./constants)

##### 例子

```javascript
import { ColumnTypes } from 'seatable-api';

await base.modifyColumnType('Table1', 'nePI', ColumnTypes.NUMBER)
```

#### Add column options

单选，多选列专用，添加选项

```javascript
base.addColumnOptions(table_name, column, options)
```

##### 例子

```javascript
await base.addColumnOptions('Table1', 'My choices', [
        {"name": "ddd", "color": "#aaa", "textColor": "#000000"},
        {"name": "eee", "color": "#aaa", "textColor": "#000000"},
        {"name": "fff", "color": "#aaa", "textColor": "#000000"},
])
```

#### Add column cascade settings

单选列专用，添加单选选项的父子及联关系，达到子列的单选选项条目根据父列的选项而定的效果

```javascript
base.addColumnCascadeSettings(table_name, child_column, parent_column, cascade_settings)
```

其中

* child_column: 单选子列的名称
* parent_column: 单选父列的名称
* cascade_settings: 及联关系设置数据

##### 例子

```javascript
await base.addColumnCascadeSettings("Table1", "single-op-col-c", "single-op-col", {
  "aaa": ["aaa-1", "aaa-2"], # 如果父列选择 “aaa”， 子列只有 “aaa-1” 和 “aaa-2” 可选 
  "bbb": ["bbb-1", "bbb-2"],
  "ccc": ["ccc-1", "ccc-2"]
})
```

#### Delete column

删除列

```javascript
base.deleteColumn(table_name, column_key)
```

##### 例子

```javascript
await base.deleteColumn('Table1', 'bsKL')
```
