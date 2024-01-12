# Views

#### List views

获取一个子表的视图

```python
base.list_views(table_name)
```

其中

* table_name: 子表名称

##### 例子

```python
base.list_views('Table1')
```

#### Get a view by name

通过名称获取 视图

```python
base.get_view_by_name(table_name, view_name)
```

其中

* table_name: 子表名称
* view_name： 视图名称

##### 例子

```python
base.get_view_by_name('Table1', 'MyView')
```

#### Add view

增加视图

```python
base.add_view(table_name, view_name)
```

其中

* table_name: 子表名称
* view_name： 需要增加的视图名称


##### 例子

```python
base.add_view('Table1', 'New view')
```

#### Rename view

重命名一个视图

```python
base.rename_view(table_name, view_name, new_view_name)
```

其中

* table_name: 子表名称
* view_name： 当前视图名称
* new_view_name： 需要更新的名称

##### 例子

```python
base.rename_view('Table1', 'MyView', 'NewView')
```

#### Delete view

删除一个视图

```python
base.delete_view(table_name, view_name)
```

其中

* table_name: 子表名称
* view_name：需要删除的视图的名称

##### 例子

```python
base.delete_view('Table1', 'MyView')
```

