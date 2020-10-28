# Constants

在脚本中可能会有一些常量需要我们了解下

## ColumnTypes

列类型，当插入/追加列、更改列类型时等情况需要使用到

```python
from seatable_api import ColumnTypes

ColumnTypes.NUMBER              # 数字
ColumnTypes.TEXT                # 文本
ColumnTypes.LONG_TEXT           # 长文本
ColumnTypes.CHECKBOX            # 勾选
ColumnTypes.DATE                # 日期时间
ColumnTypes.SINGLE_SELECT       # 单选
ColumnTypes.MULTIPLE_SELECT     # 多选
ColumnTypes.IMAGE               # 图片
ColumnTypes.FILE                # 文件
ColumnTypes.COLLABORATOR        # 协作人
ColumnTypes.LINK                # 链接其他记录
ColumnTypes.FORMULA             # 公式
ColumnTypes.CREATOR             # 创建者
ColumnTypes.CTIME               # 创建时间
ColumnTypes.LAST_MODIFIER       # 修改者
ColumnTypes.MTIME               # 修改时间
ColumnTypes.GEOLOCATION         # 地址
ColumnTypes.AUTO_NUMBER         # 自动序号
ColumnTypes.URL                 # 链接
```
