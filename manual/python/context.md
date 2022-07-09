# Context

当脚本在云端运行时, context 对象提供了上下文环境。使用方法如下

```Python
from seatable_api import context

context.server_url # 服务器地址，用于初始化 Base
context.api_token  # 访问一个 base 用的 API token
context.current_table  # 用户手工运行一个脚本的时候，当前用户正在查看的表格名
context.current_row # 用户手工运行一个脚本的时候，当前光标所在的行
context.current_user_id # 手动运行脚本的用户ID
```
