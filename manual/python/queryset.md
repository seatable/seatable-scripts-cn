# QuerySet

QuerySet 通过调用 filter 函数，并且传入类 sql 的查询语句，可以简化对记录的操作。关于查询语句的规范请参考

* [查询语句规范](query-sentences.md)

#### Get a queryset

根据删选条件获取特定的记录，返回一个 QuerySet。

```python
base.filter(table_name, conditions="", view_name=None)
```

**注意: 如果未指定视图，将默认使用子表的第一个视图**

##### 例子

```python
queryset = base.filter("Table1", "")
queryset = base.filter("Table1", "年龄>18")
queryset = base.filter("Table1", "年龄>18", view_name="default")
```

#### Filter

进一步过滤行

```python
queryset.filter(conditions)
```

##### 例子

```python
new_queryset = queryset.filter("性别='女' and '工作 地点'='北京' and 年龄<=65")
new_queryset = queryset.filter("性别='女' or '工作 地点'='北京'")
new_queryset = queryset.filter("性别='女' and '工作 地点'!='北京'")
```

#### Get a single row

过滤获取单一行

```python
queryset.get(conditions)
```

##### 例子

```python
row = queryset.get("姓名=小红")
```

#### Copy queryset

复制QuerySet

```python
queryset.all()
```

##### 例子

```python
new_queryset = queryset.all()
```

#### Update rows

批量更新行

```python
queryset.update(row_data)
```

##### 例子

```python
row_data = {'工作 地点': '上海'}
new_rows = queryset.update(row_data)
```

#### Delete rows

批量删除行

```python
queryset.delete()
```

##### 例子

```python
count = queryset.delete()
```

#### Get a row

获取某行

```python
for row in queryset:
    print(row)

queryset.first()

queryset.last()

queryset[index]
```

##### 例子

```python
for row in queryset:
    print(row)

row = queryset.first()

row = queryset.last()

row = queryset[1]
```

#### Attributes

属性

```python
queryset.count()

len(queryset)

queryset.exists()

if queryset:
    print('True')
```

##### 例子

```python
count = queryset.count()

count = len(queryset)

exists = queryset.exists()

if queryset:
    print('True')
```
