import os
import time
import barcode
from barcode.writer import ImageWriter
from seatable_api import Base, context
"""
该脚本展示把行的文本等内容，转换成条码并存入表格图片列的过程.
"""

api_token = context.api_token or "859ad340d9a2b11b067c11f43078992e14853af5"
server_url = context.server_url or "https://cloud.seatable.cn"

TEXT_COL = "Message"
BARCODE_IMAGE_COL = "BarcodeImage"
TABLE_NAME = 'Table1'
BARCODE_TYPE = 'code128'

CUSTOM_OPTIONS = {
    "module_width": 0.2,       # 单个条纹的最小宽度, mm
    "module_height": 15.0,     # 条纹带的高度, mm
    "quiet_zone": 6.5,         # 图片两边与首尾两条纹之间的距离, mm
    "font_size": 10,           # 条纹底部文本的大小,pt
    "text_distance": 5.0,      # 条纹底部与条纹之间的距离, mm
}


CODE = barcode.get_barcode_class(BARCODE_TYPE)
base = Base(api_token, server_url)
base.auth()

def get_time_stamp():
    return str(int(time.time()*100000))

for row in base.list_rows(TABLE_NAME):
    row_id = row.get('_id')
    msg = str(row.get(TEXT_COL))

    # 生成条码对象
    code_img = CODE(msg, writer=ImageWriter())
    save_name = "%s_%s" % (row_id, get_time_stamp())

    # 保存为图片并暂存
    file_name = code_img.save("/tmp/%s" % save_name, options=CUSTOM_OPTIONS)

    # 将图片上传至 Base 表格
    info_dict = base.upload_local_file(file_name, name=None, file_type='image', replace=True)
    img_url = info_dict.get('url')
    row[BARCODE_IMAGE_COL] = [img_url]
    base.update_row('Table1', row_id, row)

    # 移除暂存文件
    os.remove(file_name)
