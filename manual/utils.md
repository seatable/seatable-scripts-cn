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
base.lookupAndCopy(sourceTableName, sourceColumnName, sourceColumnToCompare, targetTable, targetColumn, targetColumnToCompare = null);
```

查找一个子表中的某一列中特定的数据, 将另一个表中指定列的特定数据依次替换为这些数据, 如果方法中没有指明要替换的内容, 查找到的数据会以新行的形式插入到表格中

##### 例子

```javascript
  // 将 Table1 中的 Name 列中内容为 'name1' 的单元格插入到 Table2 的 Name 列.
  base.lookupAndCopy('Table1', 'Name', 'name1', 'Table2', 'Name');

  // 将 Table2 的 Name 列中内容为 'name2' 的单元格依次替换成 Table1 中 Name 列内容为 'name1'的单元格.
  base.lookupAndCopy('Table1', 'Name', 'name1', 'Table2', 'Name', 'name2');
```