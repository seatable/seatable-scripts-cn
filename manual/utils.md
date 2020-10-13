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
base.lookupAndCopy(targetTable, targetColumn, targetColumnToCompare, sourceTableName, sourceColumnName, sourceColumnToCompare = null);
```

搜索表格中指定的某一列的数据, 找到符合条件的数据, 并填写到表格中

##### 例子

```javascript
  
  // 匹配出 Table1 和 Table2 中 Name 列的内容相同的行, 将 Table1 中的行的 Email 列的内容到 Table2 中对应行的 Email 列
  base.lookupAndCopy('Table2', 'Email', 'Name', 'Table1', 'Name');
  
  // 匹配出 Table1 中 Name 列和 Table2 中 Name1 列的内容相同的行, 将 Table1 中的行的 Email 列的内容到 Table2 中对应行的 Email1 列
  base.lookupAndCopy('Table2', 'Email1', 'Name1', 'Table1', 'Email', 'Name');
```