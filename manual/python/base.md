# Base 对象

Base 代表一个表格。你可以用两种方法来获取读写一个 base 的授权。一个是使用单个表格的 api token, 这个 token 可以在网页端直接生成。在云端环境下从 context.api_token 直接读取。

还有一个方法是使用账号名和密码来初始化一个 Account 对象，然后调用 Account 的接口来获取一个 base 对象。第一种方法更加安全一些。

## 获取授权

使用表格的 API Token 来获取一个 base 的访问授权。

##### 例子

```
from seatable_api import Base, context

server_url = context.server_url or 'https://cloud.seatable.cn'
apt_token = context.api_token or 'c3c75dca2c369849455a39f4436147639cf02b2d'

base = Base(api_token, server_url)
base.auth()
```

## Base 上的操作

Base 对象提供了操作行和列，上传下载文件等的接口，请参考文档

* [Rows](rows.md)
* [Links](links.md)
* [Columns](columns.md)
* [Files](files.md)

