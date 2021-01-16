# Utility 方法

Utility 方法可以帮助你处理 SeaTable 中的数据.

### formatDate

格式化日期, 返回一个 ‘YYYY-MM-DD’ 格式的日期

##### 例子

```javascript
let date = new Date();
let formatDate = base.utils.formatDate(date);

output.text(formatDate); // 2020-08-20
```

### formatDateWithMinutes

格式化日期, 返回一个 ‘YYYY-MM-DD HH:mm’ 格式的日期

##### 例子

```javascript
let date = new Date();
let formatDate = base.utils.formatDateWithMinutes(date);

output.text(formatDate); // 2020-08-20 14:00
```

### lookupAndCopy（）

```javascript
base.utils.lookupAndCopy(targetTable, targetColumn, targetColumnToCompare, sourceTableName, sourceColumnName, sourceColumnToCompare = null);
```

类似 Excel 中 vlookup 函数。为目标表格的每一行在源表格中查找匹配的行，然后把匹配行的指定单元格的数据拷贝到目标行指定的单元格中。

比如我们有一个源表格包含了用户名和邮件地址的对应关系:

| Name | Email | 
|-----|-------|
| xxx | xxxx |
| yyy | yyyy |

目标表格只有用户名

| Name | Email | 
|-----|-------|
| xxx |       |
| yyy |       |

我们需要把源表格中的 Email 信息拷贝到目标表格中，那么就可以用这个函数。

##### 例子

```javascript
  
  // 匹配出 Table1 和 Table2 中 Name 列的内容相同的行, 将 Table1 中的行的 Email 列的内容拷贝到 Table2 中对应行的 Email 列
  base.utils.lookupAndCopy('Table2', 'Email', 'Name', 'Table1', 'Name');
  
  // 匹配出 Table1 中 Name 列和 Table2 中 Name1 列的内容相同的行, 将 Table1 中的行的 Email 列的内容拷贝到 Table2 中对应行的 Email1 列
  base.utils.lookupAndCopy('Table2', 'Email1', 'Name1', 'Table1', 'Email', 'Name');
```

### query

通过类 sql 语句的方式对表格数据进行筛选并归总

#### 例子

```javascript
 // 过滤出 number, number1, number2 这三列的和大于5的行, 并对这些行中的 number, number2 列分别求和, 返回结果 {number: 12, number2: 23}
 base.utils.query('Table1', 'select sum(number), sum(number2) where number + number1 + number2 > 5');
  
```

### filter

通过一个条件语句, 过滤出表格中符合条件的行, 并返回一个 querySet 对象

#### 例子

```javascript
// 过滤出 number列 等于 5 的行, 返回一个 querySet 对象
const querySet = base.utils.filter('Table1', '默认视图', 'number = 5');
```

#### querySet 对象

该对象提供了一些操作通过 filter 方法过滤得到的数据的方法

##### querySet.all

以一个列表的形式返回所有过滤得到的数据

###### 例子

```javascript
const list = querySet.all();
```

##### querySet.count

返回过滤得到的行的数量

###### 例子

```javascript
const count = querySet.count();
```

##### querySet.last

返回最后一条过滤得到的数据

###### 例子

```javascript
const row = querySet.last();
```

##### querySet.first

返回第一条过滤得到的数据

###### 例子

```javascript
const row = querySet.first();
```

##### querySet.delete

删除所有过滤得到的行, 并返回成功删除的数量

###### 例子

```javascript
const count = querySet.delete();
```

##### querySet.update

修改行数据, 并返回更新后的数据

###### 例子

```javascript
// 将过滤得到的所有的行的 Name 列的内容修改为 xxxx
const rows = querySet.update({Name: 'xxxx'});
```

##### querySet.filter

进一步进行过滤, 返回一个 querySet 对象

###### 例子

```javascript
// 过滤出 querySet 中 Name 列的值为李明的行
const querySet1 = querySet.filter('Name = "李明"');
```

##### querySet.get

获取 querySet 中的满足条件的第一条数据, 返回一个 row

###### 例子

```javascript
// 获取 querySet 中 Name 列的值为李明的第一条数据
const row = querySet.get('Name = "李明"');
```