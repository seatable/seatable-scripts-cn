import requests
from bs4 import BeautifulSoup
import re
from seatable_api import Base, context
import os
import time
'''
该脚本演示了通过从维基百科举行冬奥会的城市数据中摘取相关内容，解析，并把其填入 seatable 表格中的案例
数据包括地理位置的经纬度， 以及代表图片
'''
SERVER_URL = context.server_url or 'https://cloud.seatable.cn/'
API_TOKEN  = context.api_token  or 'cacc42497886e4d0aa8ac0531bdcccb1c93bd0f5'
TABLE_NAME = "历届举办地"
URL_COL_NAME = "维基百科城市链接"
CITY_COL_NAME = "举办城市"
POSITION_COL_NAME = "经纬度"
IMAGE_COL_NAME = "城市图片"

def get_time_stamp():
    return str(int(time.time()*10000000))

class WinterOlypic(object):

    def __init__(self, authed_base):
        self.base = authed_base
        self.soup = None

    def _convert(self, tude):
        # 把经纬度格式转换成十进制的格式，方便填入表格。
        multiplier = 1 if tude[-1] in ['N', 'E'] else -1
        return multiplier * sum(float(x) / 60 ** n for n, x in enumerate(tude[:-1]))

    def _format_position(self, corninate):
        format_str_list = re.split("°|′|″", corninate)
        if len(format_str_list) == 3:
            format_str_list.insert(2, "00")
        return format_str_list

    def _get_soup(self, url):
        # 初始化DOM解析器
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content)
        self.soup = soup
        return soup

    def get_tu_position(self, url):
        soup = self.soup or self._get_soup(url)

        # 解析网页的DOM，取出经纬度的数值， 返回十进制
        lon = soup.find_all(attrs={"class": "longitude"})[0].string
        lat = soup.find_all(attrs={"class": "latitude"})[0].string

        converted_lon = self._convert(self._format_position(lon))
        converted_lat = self._convert(self._format_position(lat))

        return {
            "lng": converted_lon,
            "lat": converted_lat
        }

    def get_file_download_url(self, url):
        # 解析一个DOM，取出其中一个图片的下载链接

        soup = self.soup or self._get_soup(url)
        src_image_tag = soup.find_all(attrs={"class": "infobox ib-settlement vcard"})[0].find_all('img')
        src = src_image_tag[0].attrs.get('src')
        return "https:%s" % src

    def handle(self, table_name):
        base = self.base
        for row in base.list_rows(table_name):
            try:
                url = row.get(URL_COL_NAME)
                if not url:
                    continue
                row_id = row.get("_id")
                position = self.get_tu_position(url)
                image_file_downlaod_url = self.get_file_download_url(url)
                extension = image_file_downlaod_url.split(".")[-1]

                image_name = "/tmp/wik-image-%s-%s.%s" % (row_id, get_time_stamp(), extension)
                resp_img = requests.get(image_file_downlaod_url)
                with open(image_name, 'wb') as f:
                    f.write(resp_img.content)
                info_dict = base.upload_local_file(
                    image_name,
                    name=None,
                    relative_path=None,
                    file_type='image',
                    replace=True
                )

                row_data = {
                    POSITION_COL_NAME: position,
                    IMAGE_COL_NAME: [info_dict.get('url'), ]
                }
                base.update_row(table_name, row_id, row_data)
                os.remove(image_name)
                self.soup = None
            except Exception as e:
                print("error", row.get(CITY_COL_NAME), e)

def run():
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()

    wo = WinterOlypic(base)
    wo.handle(TABLE_NAME)

if __name__ == '__main__':
    run()


