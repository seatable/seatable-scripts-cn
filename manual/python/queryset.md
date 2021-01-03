# QuerySet

本文档将展示通过QuerySet对象如何对行进行操作

#### get a queryset

获取QuerySet，并过滤行

```python
base.filter(table_name, conditions="", view_name=None)
```

##### 例子

```python
queryset = base.filter("Table1", "")
queryset = base.filter("Table1", "年龄>18")
queryset = base.filter("Table1", "年龄>18", view_name="default")
```

#### filter

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

#### get a single row

过滤获取单一行

```python
queryset.get(conditions)
```

##### 例子

```python
row = queryset.get("姓名=小红")
```

#### copy queryset

复制QuerySet

```python
queryset.all()
```

##### 例子

```python
new_queryset = queryset.all()
```

#### update rows

批量更新行

```python
queryset.update(row_data)
```

##### 例子

```python
row_data = {'工作 地点': '上海'}
new_rows = queryset.update(row_data)
```

#### delete rows

批量删除行

```python
queryset.delete()
```

##### 例子

```python
count = queryset.delete()
```

#### get a row

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

#### attributes

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
