## QuerySet 对象

base.filter 函数的返回值, 该对象提供了一些方法可以简化对记录的操作

#### querySet.all

以一个列表的形式返回所有过滤得到的数据

##### 例子

```javascript
const list = querySet.all();
```

#### querySet.count

返回过滤得到的行的数量

##### 例子

```javascript
const count = querySet.count();
```

#### querySet.last

返回最后一条过滤得到的数据

##### 例子

```javascript
const row = querySet.last();
```

#### querySet.first

返回第一条过滤得到的数据

##### 例子

```javascript
const row = querySet.first();
```

#### querySet.delete

删除所有过滤得到的行, 并返回成功删除的数量

##### 例子

```javascript
const count = querySet.delete();
```

#### querySet.update

修改行数据, 并返回更新后的数据

##### 例子

```javascript
// 将过滤得到的所有的行的 Name 列的内容修改为 xxxx
const rows = querySet.update({Name: 'xxxx'});
```

#### querySet.filter

进一步进行过滤, 返回一个 querySet 对象

##### 例子

```javascript
// 过滤出 querySet 中 Name 列的值为李明的行
const querySet1 = querySet.filter('Name = "李明"');
```

#### querySet.get

获取 querySet 中的满足条件的第一条数据, 返回一个 row

##### 例子

```javascript
// 获取 querySet 中 Name 列的值为李明的第一条数据
const row = querySet.get('Name = "李明"');
```