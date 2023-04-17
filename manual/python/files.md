# Files

文件操作包括文件的下载和上传，其分别都有两种方式的 API 调用，一种方式是便捷方式，而另一种方式是分步方式即将下载/上传的过程： 1. 获取链接， 2. 请求该链接进行下载/上传， 进行拆分，适用于复杂的场景，比如文件批量下载、大文件上传等。下面分别对以上两种方式 API 的使用方法进行详细说明。

## 文件下载

### 便捷方式

下载文件

```python
base.download_file(file_url, save_path)
```

其中

* file_url: 文件的 URL, 可以从文件单元格中获取
* save_path: 文件下载后保存的本地路径

例子如下

```python
file_url = "https://dev.seafile.com/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/aur7e-jqc19.zip"
save_path = "/tmp/files/custom.zip"
base.download_file(file_url, save_path)
```

### 分步方式

1) 通过文件的 URL 获取下载链接

```python
# 假如您从Base的数据中获取到一个文件url为
# https://dev.seafile.com/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/aur7e-jqc19.zip
# 则截取链接后半部分调用api
download_link = base.get_file_download_link('files/2020-10/aur7e-jqc19.zip')
```

2) 使用下载链接获取文件内容

```python
import requests
response = requests.get(download_link)
```

## 文件上传

### 便捷方式

#### 把内存中的内容上传为一个文件

```python
base.upload_bytes_file(name, content, file_type='file', replace=False)
```

其中

* name: 上传之后的文件名
* content: 文件的内容，是一个 bytes 对象
* file_type: image 或者 file，若不设置则默认是 file
* replace: 是否替换同名文件，默认为 False

返回内容为文件的字典信息

```
{
    'type': str, 文件类型
     'size': int, 文件大小
     'name': str, 文件名
    'url': str, 文件url路径
}
```

例子 1, 上传网络上的一个文件

```python
import requests
file_url = 'http://www.baidu.com/xxx/xxx/xxx.txt'
response = requests.get(file_url)
info_dict = base.upload_bytes_file('my_uploaded_file.txt', response.content)
```

例子 2, 上传本地的图片

```python
local_img_file = '/Users/Desktop/a.png'
with open (local_img_file, 'rb') as f:
  content = f.read()
info_dict = base.upload_bytes_file('my_uploaded_img.png', content, file_type='image')
```


#### 用文件路径上传本地的一个文件

```python
base.upload_local_file(file_path, name=None, file_type='file', replace=False)
```

其中

* file_path: 本地的文件路径
* name: 上传之后的文件名， 若为 None 则默认用本地文件名

其他参数以及返回值格式同 upload_bytes_file

例子：

```python
local_file = '/Users/Desktop/a.png'
info_dict = base.upload_local_file(local_file, name='my_uploaded_img.png', file_type='image', replace=True)
```

### 更新表格

上面的步骤只是上传了文件，我们还需要利用上述的返回字典 info_dict， 将文件/图片更新到表格中指定文件/图片列中

以更新到 base 子表名称为 “Table1” 的子表中为例

```python
# 更新到图片单元格, 列名为 img_col
img_url = info_dict.get('url')
row['img_col'] = [img_url]
base.update_row('Table1', row['_id'], row)

# 更新文件单元格, 列名为 file_col
row['file_col'] = [info_dict]
base.update_row('Table1', row['_id'], row)

# 如果 row 中已经有图片/文件， 则
row['img_col'].append([img_url])
base.update_row('TableName', row['_id'], row)
row['file_col'].append([info_dict])
base.update_row('Table1', row['_id'], row)
```

### 分步方式上传文件

获取文件上传链接以及上传路径

```python
base.get_file_upload_link()
```

返回一个字典如

```
{
  "parent_path": "/asset/3a9d8266-78.....",		
  "upload_link": "http://..../upload-api/ea44c4f4...../"
}
```

其中

* upload_link: 上传链接
* parent_path: 服务器分配的相对目录，上传文件时需要使用该路径

以将本地 /User/Desktop/file.txt 文件上传至服务器为例

```python
# 获取文件上传链接以及服务器分配的相对目录
upload_link_dict = base.get_file_upload_link()
parent_dir = upload_link_dict['parent_path']
upload_link = upload_link_dict['upload_link'] + '?ret-json=1'

# 往上传链接中上传文件
upload_file_name = "file_uploaded.txt" # 上传之后的文件名
replace = 1 # 若上传同名文件则替换
response = requests.post(upload_link, data={
    'parent_dir': parent_dir,
    'replace': 1 if replace else 0  # 如果上传过同名文件是否要替换
}, files={
    'file': (upload_file_name, open('/User/Desktop/file.txt', 'rb'))  # 要上传的文件
})
```

## 自定义目录操作

除了 Base 表格中的附件的上传和下载外， 一个 Base 中有一个自定义的文件系统叫做 自定义目录， 通过 Base 的文件管理功能模块打开。 以下定义了一些用于操作该自定义目录的 API。

#### 列出文件夹中的文件

```python
base.list_custom_assets(path)
```

##### 例子

```python
folder_dir = "/Main/photos"

base.list_custom_assets(folder_dir)
# 返回的一个字典， 包括 dir，和 file 两个字段， dir 表示目录， file 表示文件
{
  "dir": [{'name': "MyDir"}, ...]
  "file":[{'name': "sky.png"}, ....]
}
```

#### 获取文件信息

返回的信息与表格文件列存储的信息有相同的数据结构， 因此可以直接将该信息更新到表格的文件列

```python
base.get_custom_file_info(path, name)
```

##### 例子

```python
folder_dir = "/Main/"
file_name = "sky.png"
info_dict = base.get_custom_file_info(path, name) # 获取信息
row_id = "xxxx"
file_col_name = "File"
# 更新文件单元格
base.update_row('Table1', row_id, {"File": [info_dict]})
```

#### 获取文件内容

返回 一个 Bytes 类型的数据结构, 可以将其写入本地的文件中， 相当于下载

```python
base.get_custom_file_content(file_path)
```

##### 例子

```python
custom_file_path = "/Main/sky.png"
local_path = "/Users/Desktop/sky.png"
save_name = "sky.png"
content = base.get_custom_file_content(custom_file_path)
with open(local_path, 'wb') as f: # 写入本地文件
  f.write(content)
```

#### 上传本地文件到自定义目录

返回的文件信息可以直接更新到表格的附件列

```python
base.upload_local_file_to_custom_folder(self, local_path, custom_folder_path=None, name=None)
```

* local_path: 本地的文件路径
* custom_folder_path: 自定义目录的路径， 默认为 ‘/’
* name: 自定义目录中保存的文件名， 默认与在本地的文件名一致

##### 例子

```python
local_path = "/Users/Desktop/sky.png"
custom_path = "/Main/"

info_dict = base.upload_local_file_to_custom_folder(local_path， custom_path)
row_id = "xxxx"
file_col_name = "File"
# 更新文件单元格
base.update_row('Table1', row_id, {"File": [info_dict]})
```

#### 

