# Files

本文档将展示通过Base对象如何上传/下载文件

如果您对Base对象还未了解，请参考

* [Base](base.md)

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
base.upload_local_file(file_path, name=None, relative_path=None, file_type=None, replace=False)
```

##### 例子

```python
info_dict = base.upload_local_file('files/file.png', name='upload.png', relative_path=None, file_type='image', replace=True)

# 如果需要更新row，请参照 upload file in memory 例子
```
