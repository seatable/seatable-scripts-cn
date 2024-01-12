# Views

#### List views

获取子表中所有的视图信息

```javascript
base.listViews(table_name)
```

##### 例子

```javascript
const views = await base.listViews('Table1')
```

#### Get a view by name

通过视图名称来获取一个视图

```javascript
base.getViewByName(table_name, view_name);
```

##### 例子

```javascript
const view = await base.getViewByName('Table1', 'MyView');
```

#### Add view

增加一个视图

```javascript
base.addView(table_name, new_view_name);
```


##### 例子

```javascript
await base.addView('Table1', 'new_view');
```

#### Raname view

重命名一个视图

```javascript
base.renameView(table_name, view_name, new_view_name);
```

##### 例子

```javascript
await base.renameView('Table1', 'myView', 'myView-01');
```

#### Delete view

删除一个视图

```javascript
base.deleteView(table_name, view_name);
```

##### 例子

```javascript
await base.deleteView('Table1', 'MyView');
```

