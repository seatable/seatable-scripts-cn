# Files

本文档将展示通过Base对象如何上传/下载文件

如果您对Base对象还未了解，请参考

* [Base](base.md)

文件操作包括文件的下载和上传， 其分别都有两种方式的api调用， 一种方式是便捷方式，适用于脚本操作，而另一种方式是分步方式即将下载/上传的过程： 1. 获取链接， 2. 请求该链接进行下载/上传， 进行拆分，适用于比较严谨和具体的业务操作，如文件大批量处等。下面分别对以上两种方式api的使用方法进行详细说明。

### 文件下载

#### 便捷方式

**download file**

```python
base.download_file(file_url, save_path)
# file_url: Base中文件的url
# save_path: 文件下载后保存的本地路径
# 例子如下：
file_url = "https://dev.seafile.com/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/aur7e-jqc19.zip"
save_path = "/tmp/files/custom.zip"
base.download_file(file_url, save_path)
```

#### 分步方式

通过文件的url获取下载链接， **get download link by path**

```python
# 假如您从Base的数据中获取到一个文件url为
# https://dev.seafile.com/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/aur7e-jqc19.zip
# 则截取链接后半部分调用api
download_link = base.get_file_download_link('files/2020-10/aur7e-jqc19.zip')
```

请求下载链接进行文件下载， **requests库**

```python
import requests
response = requests.get(download_link)
```

### 文件上传
#### 便捷方式

上传bytes文件 ，**upload bytes file**

```python
base.upload_bytes_file(name, content, file_type=None, replace=False)
# name: 上传之后的文件名
# content: 文件的内容，是一个bytes对象
# file_type: 两种类型选择， image或者file，若不设置则默认是file
# replace: 是否替换同名文件
# return: 文件的字典信息
# {
#     'type': str, 文件类型
#     'size': int, 文件大小
#     'name': str, 文件名
#     'url': str, 文件url路径
# }

# 例子：
# 1. 上传网络文件
import requests
file_url = 'http://www.baidu.com/xxx/xxx/xxx.txt'
response = requests.get(file_url)
info_dict = base.upload_bytes_file = ('my_uploaded_file.txt', response.content, replace=False)

# 2. 上传本地文件
local_img_file = '/Users/Desktop/a.png'
with open (local_img_file, 'rb') as f:
  content = f.read()
info_dict = base.upload_bytes_file = ('my_uploaded_img.png', content, file_type='image', replace=False)
```

根据本地文件名上传， **upload local file**

```python
base.upload_local_file(file_path, name=None, file_type=None, replace=False)
# name: 上传之后的文件名， 若为None则默认取本地文件名
# file_path: 本地的文件路径， 其他参数以及返回值格式同upload_bytes_file

# 例子：
local_file = '/Users/Desktop/a.png'
info_dict = base.upload_local_file(local_file, name='my_uploaded_img.png', file_type='image', replace=True)
```

更新表格

利用上述的返回字典info_dict， 将图片更新到表格中指定文件/图片列中， 例如更新到base子表名称为“Table1”的表格中

```python
# 1. 更新行
# 假设图片的列名为img_col
img_url = info_dict.get('url')
row['img_col'].append(img_url)
base.update_row('Table1', row['_id'], row)
# 假设更新文件列, 列名为file_col
file_url = info_dict.get('url')
row['file_col'].append(file_url)
base.update_row('Table1', row['_id'], row)

# 若无图片/文件列， 则
row['img'] = [info_dict.get('url')]
# row['file'] = [info_dict]
base.update_row('TableName', row['_id'], row)

# 2. 插入新行
# 如果插入新行
new_row = {
    'img_col': [info_dict.get('url')],
    'file_col': [info_dict]
}
base.append_row('Table1', row)
```

#### 分步方式

获取base的文件上传链接以及上传路径， **get file upload link**

```python
base.get_file_upload_link()
# 返回一个字典如
# {
#  "parent_path": "/asset/3a9d8266-78.....",		#文件上传的根目录
#  "upload_link": "http://..../upload-api/ea44c4f4...../": 文件上传链接
# }
```

通过上传链接进行文件上传， **requests库**

```python
# 如需要将本地/User/Desktop/file.txt文件上传至服务器
# 1. 获取文件上传链接以及根目录
upload_link_dict = base.get_file_upload_link()
parent_dir = upload_link_dict['parent_path']
upload_link = upload_link_dict['upload_link'] + '?ret-json=1'
upload_file_name = "file_uploaded.txt" # 上传之后的文件名
replace = 1 # 若上传同名文件则替换

#请求上传链接
response = requests.post(upload_link, data={
    'parent_dir': parent_dir,
    'replace': 1 if replace else 0  # 如果上传过同名文件是否要替换
}, files={
    'file': (upload_file_name, open('/User/Desktop/file.txt', 'rb'))  # 要上传的文件
})
```
