# SeaTable 脚本编程手册

SeaTable 支持你通过编写脚本来满足个性化的需求。目前支持的脚本语言包括 Javascript 和 Python。

Javascript 脚本来当前的浏览器中直接运行，适合于对数据进行简单的处理。Python 脚本在服务器端运行，而且可以设置自动周期性运行，适合于更复杂的数据处理场景。

## 编程入门

在 SeaTable 中，一个表格英文叫做一个 base。一个 base 包括多个子表，一个子表英文叫做一个 table。一个 table 中包含多个行和列。一个行包含多个字段。

### Javascript 脚本入门

脚本执行器提供了两个基本对象供你使用:

1. base 对象。一个 base 代表一个表格。通过 base 对象可以操作表格中的数据。
2. output 对象。用于输出结果。

下面我们来看一个很简单的例子，就是输出表格中子表的数量。新建一个脚本，并输入以下的内容，然后点击运行即可:

```
const tables = base.getTables();
output.text(tables.length);
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

### Python 脚本入门

编写脚本时，需要从 seatable_api 导入 Base 对象并对其初始化，然后就可以调用其中的函数来操作表格了。下面为一个简单的例子，用于往一个表格中添加一个新行:

```
from seatable_api import Base

server_url = os.environ.get('dtable_web_url')
api_token = os.environ.get('api_token')
base = Base(api_token, server_url)
base.auth()

row_data = {
    "Name": "I am new Row"
}
base.append_row('Table1', row_data)
```

## 进一步参考

* [数据结构](data-structure.md)
* [Javascript](javascript/README.md)
* [Python](python/README.md)
