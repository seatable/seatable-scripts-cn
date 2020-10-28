# Files

本文档将展示通过Base对象如何上传/下载文件

如果您对Base对象还未了解，请参考

* [Base](base.md)

#### get downlaod link by path

获取文件下载链接

```python
# path: 文件在该Base下的相对路径
base.get_file_download_link(path)
```

##### 例子

```python
# 假如您从Base的数据中获取到一个文件url为
# https://dev.seafile.com/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/aur7e-jqc19.zip
# 则获取链接为
download_link = base.get_file_download_link('files/2020-10/aur7e-jqc19.zip')
# 如果您想要下载则使用该链接下载，例子中使用requests库，您可以使用其他库操作
response = requests.get(download_link)
```

#### get file upload link

获取上传链接以上传文件，返回一个字典，上传链接在其中
上传时，需要两个参数，parent_dir和relative_path，详情请见例子

```python
# 返回字典
# {
#     "parent_path": "xxxxx",
#     "upload_link": "https://xxxxxx"
# }
base.get_file_upload_link()
```

##### 例子

```python
upload_link_dict = base.get_file_upload_link()
# 上传文件，使用的requests库，您可以使用其他库操作
parent_dir = upload_link_dict['parent_path']
upload_link = upload_link_dict['upload_link'] + '?ret-json=1'
response = requests.post(upload_link, data={
    'parent_dir': parent_dir,
    'relative_path': relative_path,
    'replace': 1 if replace else 0  # 如果上传过同名文件是否要替换
}, files={
    'file': (name, open(file_path, 'rb'))  # 要上传的文件
})
```

单纯的API操作很简单，但是如果完整的操作

截取path，获取下载链接，下载，保存

或者

获取上传链接，读取文件，组建参数，上传

如果代码严谨一些，还要加上中间检查每个请求的状态等

非常繁琐，所以下面将会展示将上述过程封装后的下载/上传文件的API供您使用

#### download file

下载文件

```python
# 文件保存到save_path这个文件路径
base.download_file(file_url, save_path)
```

##### 例子

```python
# 将文件下载到这个文件路径
base.download_file('https://dev.seafile.com/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/screen%20(3).png', 'files/screen.png')
```

#### upload file in memory

```python
# name: 上传后的文件名
# content: 文件内容，是一个bytes对象
# relative_path: 上传的相对路径，是该base附件文件下的路径
# file_type: image or file，默认为file
# relative_path和file_type不能同时为None，如果relative_path为None，则其值为 {file_type}s/{today-month} 如 files/2020-09
# replace: 如果目录下有同名文件是否替换
# return: 返回被上传文件的信息dict
# {
#     'type': str,
#     'size': int,
#     'name': str,
#     'url': str
# }
base.upload_bytes_file(name, content: bytes, relative_path=None, file_type=None, replace=False)
```

##### 例子

```python
reponse = requests.get('http://xxxxxx.png')
info_dict = base.upload_bytes_file('file.png', response.content, file_type='file', replace=False)
with open('file.png', 'rb') as f:
    content = f.read()
info_dict = base.upload_bytes_file('file.png', content, file_type='image', replace=False)

# 如果需要更新row
# 更新图片列，假设图片列名为img，则
row['img'].append(info_dict.get('url'))
base.update_row('TableName', row['_id'], row)

# 更新文件列，假设文件列命为file，则
row['file'].append(info_dict)
base.update_row('TableName', row['_id'], row)

# 当然了，如果该行还没有图片/文件列，则
row['img'] = [info_dict.get('url')]
# row['file'] = [info_dict]
base.update_row('TableName', row['_id'], row)

# 如果插入新行
row = {
    'img': [info_dict.get('url')],
    'file': [info_dict]
}
base.append_row('real-img-files', row)
```

#### upload local file

```python
# file_path: 文件路径
# name: 上传后的文件名，如果为None, 则是文件的名字
# relative_path: 上传的相对路径，是该base附件文件下的路径
# file_type: image or file，默认为file
# relative_path和file_type不能同时为None，如果relative_path为None，则其值为 {file_type}s/{today-month} 如 files/2020-09
# replace: 如果目录下有同名文件是否替换
# return: 返回被上传文件的信息dict
# {
#     'type': str,
#     'size': int,
#     'name': str,
#     'url': str
# }
base.upload_local_file(file_path, name=None, relative_path=None, file_type=None, replace=False)
```

##### 例子

```python
info_dict = base.upload_local_file('files/file.png', name='upload.png', relative_path=None, file_type='image', replace=True)

# 如果需要更新row，请参照 upload file in memory 例子
```
