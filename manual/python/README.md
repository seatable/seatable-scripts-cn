# SeaTable Python 脚本编程

同Javascript, 脚本文件一般用于表格中数据的处理，但Python脚本由后台运行，且Python脚本中涉及到的表格读写操作由seatable-api库负责。

[seatable-api](https://pypi.org/project/seatable-api/)

## 编程入门

编写脚本时，需要引入seatable_api

```
from seatable_api import Base
```

其中Base类就是要负责与SeaTable进行交互，交互前请先进行初始化

```
from seatable_api import Base

# 此为SeaTable的地址
server_url = os.environ.get('dtable_web_url')
# 与SeaTable交互使用的api_token
api_token = os.environ.get('api_token')

# 以上两项均从环境变量中活得不必手动填写

# 使用上面定义的变量进行初始化
base = Base(api_token, server_url)
# 并登陆
base.auth()

```

如若您脚本与SeaTable交互，则以上代码应总是做为您脚本文件的前几行


可以通过简单例子看下如何操作

```
import os

from seatable_api import Base


server_url = os.environ.get('dtable_web_url')
api_token = os.environ.get('api_token')

base = Base(api_token, server_url)

base.auth()



table_name = 'Table1'

row_data = {

    "Name": "I am new Row"

}

base.append_row(table_name, row_data)
```

添加脚本并运行该代码，则会发现表格Table1增加了一空白行


## 编程参考

SeaTable 一般对象的数据结构:

* [数据结构](../data-structure.md)

SeaTable API 对象介绍:

* [Base](base.md)
