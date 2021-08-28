# Query with SQL

#### Query

使用 sql 语句查询一个 base

```python
base.query(sql)
```

其中

* sql: 要执行的 SQL 语句

##### 例子

```python
base.query('select name, price, year from Bill')
```

结果

```python
[
    {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
    {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
    {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
    {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
    {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
    {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
    {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
]
```

错误

* ValueError: sql can not be empty
* ConnectionError: network error
* Exception: no such table
* Exception: no such column

#### WHERE

##### 例子

```python
base.query('select name, price from Bill where year = 2021')
```

结果

```python
[
    {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300},
    {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200},
    {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200}
]
```

错误

* ValueError: sql can not be empty
* ConnectionError: network error
* Exception: no such table
* Exception: no such column

#### ORDER BY

##### 例子

```python
base.query('select name, price, year from Bill order by year')
```

结果

```python
[
    {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
    {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
    {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
    {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
    {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
    {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
    {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
]
```

错误

* ValueError: sql can not be empty
* ConnectionError: network error
* Exception: no such table
* Exception: no such column

#### GROUP BY

##### 例子

```python
base.query('select name, sum(price) from Bill group by name')
```

结果

```python
[
    {'SUM(price)': 600, 'name': 'Bob'},
    {'SUM(price)': 400, 'name': 'Tom'},
    {'SUM(price)': 400, 'name': 'Jane'}
]
```

错误

* ValueError: sql can not be empty
* ConnectionError: network error
* Exception: no such table
* Exception: no such column
* Exception: columns in group by should match columns in select

#### DISTINCT

##### 例子

```python
base.query('select distinct name from Bill')
```

结果

```python
[
    {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob'},
    {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom'},
    {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane'}
]
```

错误

* ValueError: sql can not be empty
* ConnectionError: network error
* Exception: no such table
* Exception: no such column
