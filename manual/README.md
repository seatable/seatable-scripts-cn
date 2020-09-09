# SeaTable 脚本编程手册

SeaTable 脚本使用 Javascript 语言编写。一个脚本一般用于表格中数据的处理。脚本可以在用户的浏览器中或者后台运行。(目前仅支持在用户的浏览器中运行)

## 编程入门

在 SeaTable 中，一个表格英文叫做一个 base。一个 base 包括多个子表，一个子表英文叫做一个 table。一个 table 中包含多个行和列。一个行包含多个字段。

脚本执行器提供了两个基本对象供你使用:

1. base 对象。一个 base 代表一个表格。通过 base 对象可以操作表格中的数据。
2. output 对象。用于输出结果。

下面我们来看一个很简单的例子，就是输出表格中子表的数量。新建一个脚本，并输入以下的内容，然后点击运行即可:

```
const tables = base.getTables();
// `${tables.length}` 把变量 tables.length 的值变成一个字符串
output.text(`${tables.length}`);
```

下面我们来看另一个简单的例子，就是取出一个子表中的所有行，然后把 Name 列的值输出出来:

```
// 通过名称获取子表
const table = base.getTableByName('云端服务'); 
// 从子表获取一个特定的视图
const view = base.getViewByName(table, 'Default View');
// 通过 table 和 view 来获取视图中所有的行
const rows = base.getRows(table, view);
// 遍历和打印
for (var i=0; i<rows.length; i++) {
  const row = rows[i];
  output.text(row['Name']);
}
```

从上面的两个例子可以看到，通过调用 base 对象特定的方法，我们就能获取表格中所有的数据了。在 base 对象对应的文档中，我们可以查找到 base 提供的所有的方法。

## 编程参考

SeaTable 脚本中用到的一些对象的数据结构:

* [数据结构](data-structure.md)

对象提供的方法:

* [base](base.md)
* [output](output.md)
* [utilities](utils.md)

## 例子

可以通过这个链接找到一些容易理解的例子[https://github.com/seatable/seatable-scripts-cn/tree/master/examples](https://github.com/seatable/seatable-scripts/tree/master/examples)

具体如下

* [get-incremental.js](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/get-incremental.js): 从一个累计列计算出增量数据
* [auto-add-rows.js](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/auto-add-rows.js): 自动往一个记账表中添加每月重复的项目
