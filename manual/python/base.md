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

Base对象提供了操作行列的方法，具体如下

## 行

#### list rows

获取表格的所有行

```python
base.list_rows(table_name, view_name=None)
```

##### 例子

```python
rows = base.list_rows('Table1')
rows = base.list_rows('Table1', view_name='default')
```

#### append row

追加表格

```python
base.append_row(table_name, row_data)
```

##### 例子

```python
row_data = {
    "Name": "I am new Row"
}

base.append_row('Table1', row_data)
```

#### insert row

插入表格

```python
base.insert_row(table_name, row_data, anchor_row_id)
# anchor_row_id为锚定的行的id，将会把新行插入到这行下方
```

##### 例子

```python
row_data = {
    "Name": "I am new Row"
}

base.insert_row('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw')
```

#### update row

更新一行

```python
base.update_row(table_name, row_id, row_data)
```

##### 例子

```python
row_data = {
    "dcXS": "123"
}
base.update_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
```

#### delete row

删除一行

```python
base.delete_row(table_name, row_id)
```

##### 例子

```python
base.delete_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### filter rows

过滤行

```python
base.filter_rows(table_name, filters, view_name=None, filter_conjunction='And')
```

##### 例子

```python
filters = [{
    "column_key":"0000",
    "filter_predicate":"contains",
    "filter_term":"a"
}],
base.filter_rows('Table1', filters=filters)
```

## 列

#### list columns

列出表/视图所有行

```python
base.list_columns(table_name, view_name=None)
```

##### 例子

```python
base.list_columns('Table1')
base.list_columns('Table1', view_name='default')
```

#### insert column

插入/追加列

```python
base.insert_column(table_name, column_name, column_type, column_key=None)
```

`column_key`为要插入的位置的前一列的key，如若省略则默认追加为最后一列

column_type请参考 [constants](../constants)

##### 例子

```python
from seatable_api.constants import ColumnTypes
base.insert_column('Table1', 'python-api', ColumnTypes.TEXT)
base.insert_column('Table1', 'python-api', ColumnTypes.TEXT, column_key=ColumnTypes.TEXT)
```

#### rename column

重命名列

```python
base.rename_column(table_name, column_key, new_column_name)
```

##### 例子

```python
base.rename_column('Table1', 'kSiR', 'new-python-api')
```

#### resize column

设置列宽

```python
base.resize_column(table_name, column_key, new_column_width)
```

##### 例子

列的默认宽度为200，如果需要调整列宽比如调整为500，则

```python
base.resize('Table1', 'asFV', 500)
```

#### freeze column

冻结列

```python
base.freeze_column(table_name, column_key, frozen)
```

frozon: True/False

##### 例子

```python
base.freeze_column('Table1', '0000', True)
```

#### move column

```python
base.move_column(table_name, column_key, target_column_key)
```

column_key为要移动的列的key

target_column_key为锚定列的key，被移动的列将会被移动到该列右边

##### 例子

```python
base.move_column('Table1', 'loPx', '0000')
```

此例中，`loPx`列将会被移动到`0000`列的右边

#### modify column type

转换列类型

```python
base.modify_column_type(table_name, column_key, new_column_type)
```

column_type请参考 [constants](../constants)

##### 例子

```python
from seatable_api.constants import ColumnTypes

base.modify_column_type('Table1', 'nePI', ColumnTypes.NUMBER)
```

#### delete column

删除列

```python
base.delete_column(table_name, column_key)
```

##### 例子

```python
base.delete_column('Table1', 'bsKL')
```

## 下载/上传文件

#### download file

下载文件

```python
base.download_file(file_url, save_path)
```

##### 例子

```python
# 将文件下载到目录files下
base.download_file('https://dev.seafile.com/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/screen%20(3).png', 'files')
```

#### upload file in memory

```python
# name: 上传后的文件名
# content: 文件内容，是一个bytes对象
# relative_path: 上传的相对路径，是该base附件文件下的路径
# file_type: image or file，默认为file
# relative_path和file_type不能同时为None，如果relative_path为None，则其值为 {file_type}s/{today-month} 如 files/2020-09
# replace: 如果目录下有同名文件是否替换
base.upload_bytes_file(name, content: bytes, relative_path=None, file_type=None, replace=False)
```

##### 例子

```python
reponse = requests.get('http://xxxxxx.png')
base.upload_bytes_file('file.png', response.content, relative_path=None, file_type='file', replace=False)
with open('file.png', 'rb') as f:
    content = f.read()
base.upload_bytes_file('file.png', content, relative_path=None, file_type='file', replace=False)
```

#### upload local file

```python
# file_path: 文件路径
# name: 上传后的文件名，如果为None, 则是文件的名字
# relative_path: 上传的相对路径，是该base附件文件下的路径
# file_type: image or file，默认为file
# relative_path和file_type不能同时为None，如果relative_path为None，则其值为 {file_type}s/{today-month} 如 files/2020-09
# replace: 如果目录下有同名文件是否替换
base.upload_local_file(file_path, name=None, relative_path=None, file_type=None, replace=False)
```

##### 例子

```python
base.upload_local_file('files/file.png', name='upload.png', relative_path=None, file_type='image', replace=True)
```
