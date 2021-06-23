# Query


#### Query With SQL

使用sql语句查询base

```python
base.query(sql)
```

其中

* sql: 要执行的sql语句

##### 例子

```python
base.query('select name,age from table')
```
返回结果

* 返回查询table的各条数据

```python
[
    {
        'name': 'liming', 
        'age': 11
     },
    {
        'name': 'liming', 
        'age': 11
    },
]
```