from seatable_api import Base, context
import uuid
import requests
import time
import os

"""
该脚本用于从图片链接下载图片到图片列。你可以在一个文本列中记录图片的地址，然后用这个
脚本自动下载图片并上传到图片列中。
"""

###################---基本信息配置---###################
SERVER_URL      = context.server_url or 'https://cloud.seatable.cn/'
API_TOKEN       = context.api_token  or 'cacc42497886e4d0aa8ac0531bdcccb1c93bd0f5'
TABLE_NAME      = 'Table1'
IMAGE_FILE_TYPE = ['jpg', 'png', 'jpeg', 'bmp', 'gif']      # 图片的格式

IMG_URL_COL     = '图片链接'                                 # 包含图片链接的列名，需要是 URL 或者文本类型 
IMG_COL         = 'img'                                     # 用于存储图片的列名，需要是图片类型

IMG_NAME_PRE    = 'image'                                   # 图片上传后使用的文件名称前缀
###################---基本信息配置---###################

def get_time_stamp():
    return str(int(time.time()*100000))
    
def img_transfer():
    # 1. 创建 base 对象并且认证
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()    

    # 2. 获取行信息, 数据结构--列表嵌套字典
    """
    数据结构例子：其中'img', '图片链接是用户自定义的列名'
    [{
        '_id': 'RNn2isDfRnSPWq5HIwRT0w',
        '_mtime': '2020-11-10T03:02:55.549+00:00',
        'Name': '冉继伟0',
        'img': [{
            'name': 'cut.png',
            'size': 2778797,
            'type': 'file',
            'url': 'https://dev.seafile.com/dtable-web/workspace/104/asset/1d50c674-ca45-4acf-85b8-19d6e10ca5f0/files/2020-11/cut.png'
        }],
        '图片链接': 'https://timgsa.baidu.com/timg?image&quality=80xxx.jpg'
    }, {
        '_id': 'b2lrBxnDSGm1LsZDQTVGhw',
        '_mtime': '2020-11-04T08:47:51.562+00:00',
        'Name': '冉继伟1'
    }, {
        '_id': 'RBUZ_g6qS_KER0EjaSclFA',
        '_mtime': '2020-11-04T09:26:45.961+00:00',
        'Name': '冉继伟2',
        'img': None
    }, ......]
    """
    rows  = base.list_rows(TABLE_NAME)
    count = 0
    #3. 遍历每一行，获取‘图片链接‘列的信息
    for row in rows:
        time_stamp = get_time_stamp()
        img_url    = row.get(IMG_URL_COL, None)
        img        = row.get(IMG_COL, None)
        try:
            #若无图片链接或者img列有数据的话跳过，防止重复添加
            if (not img_url) or img:
                continue
            #通过url链接获取文件扩展名
            img_name_extend = img_url.strip().split('.')[-1]
            img_name_extend = img_name_extend in IMAGE_FILE_TYPE and img_name_extend or 'jpg'
            #通过uuid对下载的文件进行重命名 IMG_NAME_PRE + 时间戳 + 扩展名
            img_name     = "/tmp/image-%s.%s"%(time_stamp, img_name_extend)
            #下载文件
            response = requests.get(img_url)
            if response.status_code != 200:
                raise Exception('download file error')
            with open(img_name, 'wb') as f:
                f.write(response.content)
            #文件上传
            info_dict    = base.upload_local_file(img_name, name=None, relative_path=None, file_type='image', replace=True)
            row[IMG_COL] = [info_dict.get('url')]
            base.update_row('Table1', row['_id'], row)
            #上传完成之后删除
            os.remove(img_name)

        except Exception as err_msg:
            print('count%s-%s-%s-message: %s' % (count, row['_id'], img_url, err_msg))      #发现异常打印行数等信息方便回查
            continue
        count += 1
        
if __name__ == "__main__":
    img_transfer()

