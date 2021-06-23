# Query


#### Query With SQL

使用sql语句查询base

```python
base.query(src, sql)
```

其中

* src: 查询数据的来源 dtable-server 查询数据；storage 指定查询已经归档的数据；all 表示将两个来源的结果合并返回
* sql: 要执行的sql语句

##### 例子

```python
base.query('dtable-server', 'select name from table')
```
