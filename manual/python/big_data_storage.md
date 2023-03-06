# Big data storage

以下的方法可以对大数据存储中的已授权 Base 进行操作， 在调用方法之前， 请在界面上的大数据管理中开启大数据功能。

#### Insert rows into big data storage

批量插入行到大数据存储

```python
base.big_data_insert_rows(table_name, rows_data)
```

其中

* table_name: 子表名称


##### 例子

```python
rows = [
        {'名称': "A"},
        {'名称': "B"}
    ]

base.big_data_insert_rows('Table1', rows_data=rows)
```

#### 

