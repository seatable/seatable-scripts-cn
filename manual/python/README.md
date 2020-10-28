# SeaTable Python 脚本编程

Javascript 脚本来当前的浏览器中直接运行，适合于对数据进行简单的处理。Python 脚本在服务器端运行，而且可以设置自动周期性运行，适合于更复杂的数据处理场景。

Python 脚本也可以在你的本地机器上运行，也可以上传到 SeaTable 云端运行。本地运行方便你开发调试。

## 如何让脚本同时支持本地云端中运行

脚本在云端运行的时候会提供一个 context 对象，里边包含了系统自动给你生成的服务器的地址和 base 的 API token。如果你在本地运行则需要手工指定这两个变量；其中 API token 可以在表格的下拉菜单 "Advanced -> API Token" 中生成。

用以下的写法来支持脚本同时在本地和云端运行

```Python
from seatable_api import Base, context

server_url = context.server_url or 'https://cloud.seatable.cn'
apt_token = context.api_token or 'c3c75dca2c369849455a39f4436147639cf02b2d'


base = Base(api_token, server_url)
base.auth()
```


## 编程参考

SeaTable 一般对象的数据结构:

* [数据结构](../data-structure.md)

SeaTable API 库介绍:

* [Base](base.md)
* [Rows](rows.md)
* [Links](links.md)
* [Columns](columns.md)
* [Files](files.md)
* [Context](context.md)

