# SeaTable Python 脚本编程

Javascript 脚本在当前的浏览器中直接运行，适合于对数据进行简单的处理。Python 脚本在服务器端运行，而且可以设置自动周期性运行，适合于更复杂的数据处理场景。

Python 脚本也可以在你的本地机器上运行，也可以上传到 SeaTable 云端运行。本地运行方便你开发调试，也可以方便的把脚本集成到更大的项目中。

## 如何让脚本同时支持本地云端中运行

脚本在云端运行的时候会提供一个 context 对象，里边包含了系统自动给你生成的服务器的地址和 base 的 API token。如果你在本地运行则需要手工指定这两个变量；其中 API token 可以在表格的下拉菜单 "高级 -> API Token" 中生成。

用以下的写法来支持脚本同时在本地和云端运行

```Python
from seatable_api import Base, context

server_url = context.server_url or 'https://cloud.seatable.cn'
api_token = context.api_token or 'c3c75dca2c369849455a39f4436147639cf02b2d'


base = Base(api_token, server_url)
base.auth()
```

如果你在云端编写的话，可以复制一下内容快速开始编写:

```
from seatable_api import Base, context

base = Base(context.api_token, context.server_url)
base.auth()
```


## 本地运行需要安装的库

脚本在本地运行的时候需要安装 `seatable-api`。

```
pip3 install seatable-api
```

要求

* Python >= 3.5
* requests
* socketIO-client-nexus

## 一个简单的例子

下面的例子展示怎么在一个 base 中查询数据和更新数据。

```
base = Base(api_token, server_url)
base.auth()

queryset = base.filter('Table1', "age>18 and gender='male'")
elder_queryset = queryset.filter("age > 70")
for row in elder_queryset:
    print(row)

update_row_data = {'paid': True}
updated_rows = elder_queryset.update(update_row_data)

deleted_count = elder_queryset.delete()
```

## 编程参考

SeaTable 中对象的数据结构:

* [数据结构](../data-structure.md)

SeaTable API 库介绍:

* [Base](base.md)
* [QuerySet](queryset.md)
* [Rows](rows.md)
* [Links](links.md)
* [Columns](columns.md)
* [Files](files.md)
* [Account](account.md)
* [Context](context.md)
* [Constants](constants.md): 一些常量定义
* [云端环境下支持的库](libs.md): 云端环境下支持导入的 Python 库列表
* [QuerySet查询语句规范](query-sentences.md)


## 例子

可以通过这个链接找到一些容易理解的例子[https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python)

具体如下

* [send_email.py](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python/send_email.py): 读取一个表中的图片/文件作为附件发送邮件给另一个表中的联系人
* [image_transfer.py](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python/image_transfer.py): 从一个记录图片 URL 列表列下载图片并添加到表格中
* [verify_records.py](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python/verify_records.py): 根据记录的创建时间判断记录的有效性，并写到一列上
* [sync_mysql.py](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python/sync_mysql.py): 将mysql数据库中的信息同步至表格中
* [update_certification_expiration.py](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python/update_certification_expiration.py): 更新网站证书过期时间
* [send_wechat_msg.py](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python/send_wechat_msg.py): 通过企业微信群机器人推送群消息
* [sync_stock_price.py](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python/sync_stock_price.py): 更新股票价格信息
* [sync_data_by_spider.py](https://github.com/seatable/seatable-scripts-cn/tree/master/examples/python/sync_data_by_spider.py): 通过爬取维基百科信息写入表格

