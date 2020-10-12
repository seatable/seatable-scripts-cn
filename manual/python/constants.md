# Constants

在脚本中可能会有一些常量需要我们了解下

## ColumnTypes

列类型，继承了Python的Enum类，当插入/追加列、更改列类型时等情况需要使用到，且必须使用

```python
lass ColumnTypes(Enum):
    NUMBER = 'number'
    TEXT = 'text'
    CHECKBOX = 'checkbox'
    DATE = 'date'
    SINGLE_SELECT = 'single-select'
    LONG_TEXT = 'long-text'
    IMAGE = 'image'
    FILE = 'file'
    MULTIPLE_SELECT = 'multiple-select'
    COLLABORATOR = 'collaborator'
    LINK = 'link'
    FORMULA = 'formula'
    CREATOR = 'creator'
    CTIME = 'ctime'
    LAST_MODIFIER = 'last-modifier'
    MTIME = 'mtime'
    GEOLOCATION = 'geolocation'
    AUTO_NUMBER = 'auto-number'
    URL = 'url'
```
