# Context

当脚本在云端运行时, context 对象提供了上下文环境。context 对象提供了以下


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
