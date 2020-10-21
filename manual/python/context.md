# Context

本节将介绍一个特殊的对象 `context`，从我们之前的介绍中，您应该了解了SeaTable的基本操作并知晓了如何在云端运行脚本。

### Auth info

其中关键的第一步就是Base的授权登录 `base.auth()`，在调用这个函数之前初始化的时候需要设置`API Token`, `dtable_web_url`。如果脚本在本地运行需要手动设置两个参数，而在云端运行则从环境变量中获得。

云端如下初始化

```
import os
from seatable_api import Base

api_token = os.environ('api_token')
dtable_web_url = os.environ('dtable_web_url')
base = Base(api_token, dtable_web_url)
base.auth()
```

略微繁琐，而如果使用 `context` 对象，则可以直接从 `context` 对象中获取

```
from seatable_api import Base, context

base = Base(context.api_token, context.dtable_web_url)
base.auth()
```

除此以外，`context` 对象还提供脚本运行时针对的子表，行信息，详见如下

### 当前表

脚本运行时，可能需要读取表格，不使用 `context` 对象，需要调用 `base.list_rows(table_name, view_name)`, `base.get_metadata()` 等方法组合使用，`context` 对象则可以直接获取整个表格对象

```
from seatable_api import context

context.current_table
```

### 当前行

当脚本运行只针对某一行时的操作，则可以从 `context` 对象中获取当前行的信息

```
from seatable_api import context

context.current_row
```

**请注意：`context` 对象主要针对云端运行的脚本，除了`dtable_web_url`, `api_token`从环境变量中获取(如果您在本地设置了这两个变量，context对象依旧可以获取这两个变量的值)，其他变量本地运行时不可获得**
