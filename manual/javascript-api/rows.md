# Row

#### List rows

获取表格的所有行

```javascript
base.listRows(table_name, view_name='', order_by='', desc='', start='', limit='')
```

其中

* table_name: 子表名称
* view_name: 视图名称， 如果设定， 会返回满足视图设定条件的行数据
* order_by: 按照某列排序的列名
* desc:  是否是降序，默认为 false
* start: 索引的起始位置，行号
* limit: 数据的显示数量，最大返回 1000 行 (即使设定值超过 1000 行)

##### 例子

```javascript
const rows1 = await base.listRows('Table1')
const rows2 = await base.listRows('Table1', 'Default', '年龄', true, 5, 20)
```

#### Get row

获取表格的某一行

```javascript
base.getRow(table_name, row_id)
```

##### 例子

```javascript
const row = await base.getRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Append row

追加行

```javascript
base.appendRow(table_name, row_data, apply_default = false)
```

##### 例子

```javascript
row_data = {
    "Name": "I am new Row"
}

await base.appendRow('Table1', row_data)
```

#### Insert row

插入行

```javascript
base.insertRow(table_name, row_data, anchor_row_id, apply_default = false)
```

其中

* anchor_row_id: 锚定的行的 id，将会把新行插入到这行下方

##### 例子

```javascript
row_data = {
    "Name": "I am new Row"
}

await base.insertRow('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Batch append rows

批量追加行

```javascript
base.batchAppendRows(table_name, rows_data, apply_default = false)
```

##### 例子

```javascript
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
await base.batchAppendRows('Table6', rows_data)
```

#### Update row

更新一行

```javascript
base.updateRow(table_name, row_id, row_data)
```

##### 例子

```javascript
row_data = {
    "dcXS": "123"
}
await base.updateRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
```

#### Batch update rows

批量更新行

```javascript
base.batchUpdateRows(table_name, rows_data)
```

##### 例子

```javascript
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
await base.batchUpdateRows('Table1', rows_data=updates_data)
```

#### Delete row

删除一行

```javascript
base.deleteRow(table_name, row_id)
```

##### 例子

```javascript
await base.deleteRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Batch delete rows

批量删除行

```javascript
base.batchDeleteRows(table_name, row_ids)
```

##### 例子

```javascript
const del_rows = rows.slice(0, 3);
const row_ids = del_rows.map(row => row._id);
await base.batchDeleteRows('Table1', row_ids)
```
