# SeaTable Javascript 脚本编程

Javascript 脚本来当前的浏览器中直接运行，适合于对数据进行简单的处理。

脚本执行器提供了两个基本对象供你使用:

1. base 对象。一个 base 代表一个表格。通过 base 对象可以操作表格中的数据。
2. output 对象。用于输出结果。

## 编程参考

SeaTable 一般对象的数据结构:

* [数据结构](data-structure.md)

对象提供的方法:

* [base](javascript/base.md)
* [output](javascript/output.md)
* [utilities](javascript/utils.md)

## 例子

可以通过这个链接找到一些容易理解的例子[https://github.com/seatable/seatable-scripts-cn/tree/master/examples](https://github.com/seatable/seatable-scripts/tree/master/examples)

具体如下

* [get-incremental.js](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/get-incremental.js): 从一个累计列计算出增量数据
* [auto-add-rows.js](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/auto-add-rows.js): 自动往一个记账表中添加每月重复的项目
