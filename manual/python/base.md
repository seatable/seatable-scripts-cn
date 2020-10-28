# Base 对象

Base 提供了授权、操作数据等方法

## 授权

### auth

使用 API Token 进行登录，与 SeaTable 进行操作前必须进行此操作

##### 例子

```
from seatable_api import Base


server_url = os.environ.get('dtable_web_url')
api_token = os.environ.get('api_token')

base = Base(api_token, server_url)

base.auth()
```

Base对象提供了操作行列，上传下载文件等的接口，请参考文档

* [Rows](rows.md)
* [Links](links.md)
* [Columns](columns.md)
* [Files](files.md)

