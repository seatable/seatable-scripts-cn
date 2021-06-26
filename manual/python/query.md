# Query with SQL

使用 sql 语句查询一个 base

```python
base.query(sql)
```

其中

* sql: 要执行的 SQL 语句

##### 例子

```python
base.query('select name,age from table')
```

##### 返回结果

**成功**

返回一个 rows 列表

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

**失败**

抛出以下异常:

* ValueError: 'sql can not be empty.'
* ConnectionError: 网络错误
* Exception: 其他错误
