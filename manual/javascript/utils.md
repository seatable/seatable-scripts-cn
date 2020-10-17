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
  base.lookupAndCopy('Table2', 'Email', 'Name', 'Table1', 'Name');
  
  // 匹配出 Table1 中 Name 列和 Table2 中 Name1 列的内容相同的行, 将 Table1 中的行的 Email 列的内容拷贝到 Table2 中对应行的 Email1 列
  base.lookupAndCopy('Table2', 'Email1', 'Name1', 'Table1', 'Email', 'Name');
```
