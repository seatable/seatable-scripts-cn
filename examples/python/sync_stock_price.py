from seatable_api import Base, context
import requests

API_TOKEN = context.api_token or "cd12c956c6d999cdc487242d50db979f4ec69e74"
SERVER_URL = context.server_url or "https://dev.seatable.cn/"

STOCK_BASE_URL = 'https://api.arvinx.com/api'


TABLE_NAME = "股票"
VIEW_NAME = None

"""
该脚本用于更新表格中关注的股票价格等信息。
"""


def get_access_token():
    '''
    获取股票市场信息的入口token
    :return:
    '''
    res = requests.get("%s/stocks/token/" % STOCK_BASE_URL)
    if res.json().get('success'):
        return res.json().get('data', {}).get('token')
    return None

def get_stock_data_by_code(code, token=None):
    """

    :param code: 股票编码， 如'SZ002304'等
    :param token: 入口token
    :return: 返回相应的股票信息，包括当前价格，开盘价等
    """
    if token:
        price_url = "%s/stocks/%s?token=%s" % (STOCK_BASE_URL, code, token)
        res = requests.get(price_url)
        if res.json().get('success'):
            return res.json().get('data', None)
    return None

def get_stock_current_price(code, token=None):
    # 获取股票编码为code的当前股票价格
    stock_data = get_stock_data_by_code(code, token)
    if stock_data:
        return stock_data.get('current', None)
    return None



def update_stock_price(base):
    # 更新base表格中的当前股价
    token = get_access_token()
    for row in base.list_rows(TABLE_NAME, view_name=VIEW_NAME):
        stock_name = row.get('股票名称')
        stock_code = row.get('代码')
        current_price = get_stock_current_price(stock_code, token)
        if not current_price:
            print("[Failed!!] %s: %s 价格更新成功更新失败" % (stock_name, stock_code))
            continue
        base.update_row(TABLE_NAME, row.get('_id'), {"当前股价": current_price})
        print("[Success] %s: %s 价格更新成功更新成功" % (stock_name, stock_code))

if __name__ == '__main__':
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()
    update_stock_price(base)
