import hashlib
import requests
import hmac
import time
import json
from seatable_api import Base, context

"""
该脚本用于跨境电商网站shopee向seatable进行授权店铺的销售数据等信息同步，通过shopee开发者平台
的api以及seatable_api的结合交互， 实现数据同步。
"""

BASE_URL_LIVE = "https://partner.shopeemobile.com"     # shopee 线上正式域名
BASE_URL_TEST_NEW = "https://partner.test-stable.shopeemobile.com"  # shopee 新版测试域名
BASE_URL_TEST_OLD = "https://partner.uat.shopeemobile.com"   # shopee 老版测试域名

# 平台开发者申请之后会有一个指定且唯一的 partner_id 和 partner_key， 用于店铺授权， api调用等
PARTNER_ID = 0
PARTNER_KEY = ""

SHOP_LIMITS = 5 # 测试的店铺数量， 若要导入所有的授权店铺，设置为-1
N_DAYS_BEFORE = 2 # 测试多少天之前的订单，最高设置为 半个月之前 设置为 15
SHOP_ID_LIST = [] # 测试指定店铺数据

# base表格模版基本信息, 包括两个子表， 订单产品和订单
ORDER_ITEM_TABLE = "订单产品" # 订单产品表格名称
ORDER_TABLE = "订单"  # 订单表格名称
COL_LINK_ORDER = "订单链接"

class Shoppy(object):
    """
    封装的shopee-api请求： 包括
    1. 通过加密签名方式构造请求头
    2. 构造url
    3. post
    """

    BASE_URL = BASE_URL_LIVE

    def __init__(self, partner_id, secret_key, shop_id=None):

        self.partner_id = partner_id
        self.secret_key = secret_key
        self.shop_id = shop_id

    @property
    def _timestamp(self):
        return int(time.time())

    def _make_url(self, uri):
        """
        The full url including base url and uri, uri is the sub-domain such as
        "/api/v1/xxx/xxxx"
        :param uri:
        :return:
        """
        return "%s/%s" % (
            self.BASE_URL.rstrip('/'),
            uri.lstrip('/')
        )

    def _make_sign(self, uri, request_body):
        """
        make authorization's token put in request header
        :param uri:
        :param request_body:
        :return:
        """
        url = self._make_url(uri)
        base_string = url + "|" + json.dumps(request_body)
        sign = hmac.new(self.secret_key.encode(), base_string.encode(), hashlib.sha256).hexdigest()
        return sign

    def _generate_body(self, **kwargs):
        params = {
            "partner_id": self.partner_id,
            "timestamp": self._timestamp
        }
        if kwargs:
            params.update(kwargs)
        return params


    def _headers(self, uri, body):
        return {
            "Content-Type": "application/json",
            "Authorization": self._make_sign(uri, body)
        }

    def post(self, uri, **kwargs):
        request_body = self._generate_body(**kwargs)

        url = self._make_url(uri)
        request_headers = self._headers(uri, request_body)
        resp = requests.post(url, json=request_body, headers=request_headers)

        res_dict = resp.json()
        if res_dict.get('error'):
            result = None
        else:
            result = res_dict
        return result

class ShopManager(object):

    '''
    通过 partner_id, partner_key 获取所有的授权店铺的列表
    '''

    def __init__(self, partner_id, partner_key):
        self.api = Shoppy(partner_id, partner_key)

    def get_shops_by_partner(self):
        return self.api.post('/api/v1/shop/get_partner_shop')



class Shop(object):

    """
    通过 partner_i, partner_key, shop_id获取一个店铺，从而可以进行：
    1. 店铺信息查看
    2. 店铺订单查看
    3. 店铺订单产品查看
    ...
    """

    def __init__(self, partner_id, partner_key, shop_id):

        self.api = Shoppy(partner_id, partner_key, shop_id)
        self.shop_id = shop_id

    def _generate_timestamp(self, dt):
        timeArray = time.strptime(dt, "%Y-%m-%d")
        # 转换成时间戳
        timestamp = time.mktime(timeArray)
        return timestamp


    def get_shop_info(self):
        return self.api.post('/api/v1/shop/get', shopid=self.shop_id)

    def get_shop_orders(self, n_days_before=15):
        create_time_to = int(time.time())
        create_time_from = create_time_to - n_days_before * 24 * 3600
        return self.api.post('/api/v1/orders/basics',
                             shopid=self.shop_id,
                             create_time_from=create_time_from,
                             create_time_to=create_time_to)

    def get_order_detail(self, ordersn):
        return self.api.post('/api/v1/orders/detail',
                             shopid=self.shop_id,
                             ordersn_list = [ordersn,])

    def get_shop_order_details(self, n_days_before=14):
        order_list = self.get_shop_orders(n_days_before).get('orders')
        ordersn_list = order_list and [o.get("ordersn") for o in order_list] or []
        if not ordersn_list:
            return None
        return self.api.post('/api/v1/orders/detail',
                             shopid=self.shop_id,
                             ordersn_list=ordersn_list,
                            )

    def get_item_detail(self, item_id):
        return self.api.post('/api/v1/item/get', shopid=self.shop_id, item_id=item_id)


    def get_escow_released_orders(self):
        create_time_to = int(time.time())
        create_time_from = create_time_to - 30 * 24 * 3600
        return self.api.post('/api/v2/orders/get_escrow_detail' , shopid=self.shop_id,
                             release_time_from = create_time_from,
                             release_time_to = create_time_to
                             )



def _get_authed_shop_id(limits=-1):
    """
    获取合作授权的店铺id列表
    :return:
    """
    shop_manager = ShopManager(test_partner_id, test_api_key)
    resps = shop_manager.get_shops_by_partner()
    shop_id_list = [m.get('shopid') for m in resps.get('authed_shops')[:limits]]
    return shop_id_list

def timestamp2str(timest):
    time_obj = time.localtime(timest)
    time_str = time.strftime("%Y-%m-%d %H:%M", time_obj)
    return time_str

def insert_valid_infos_to_table(base, shop_limits=2, n_days_before=2, shop_id_list = None):
    """
    数据同步至seatable中指定的base
    """

    # 按照授权店铺-->具体店铺-->店铺订单-->订单项商品的不同level层级深入
    row_infos = [(row.get('订单编号'), row.get('下单时间')) for row in base.list_rows(ORDER_TABLE)]
    # level 0: 授权店铺
    if shop_id_list:
        shop_ids = shop_id_list
    else:
        shop_ids = _get_authed_shop_id(shop_limits)
    for shop_id in shop_ids:
        shop = Shop(test_partner_id, test_api_key, shop_id)
        shop_info = shop.get_shop_info()
        #根据excel表构造字段
        if not shop_info:
            continue

        # level 2: 店铺中订单信息, 包括订单编号， 币种， 下单时间
        orders = shop.get_shop_order_details(n_days_before=n_days_before)
        if not orders:
            continue
        order_details = orders.get('orders')
        for order_detail in order_details:
            order_sn = order_detail.get('ordersn')
            currency = order_detail.get('currency')
            time_order = timestamp2str(order_detail.get('create_time'))
            if (order_sn, time_order) in row_infos:
                #如果订单已经存在， 跳过
                continue
            # 构造订单链接
            row_data_order = {
                # shop 信息
                '店铺编号': shop_info.get('shop_id'),
                '店铺名称': shop_info.get('shop_name'),
                '站点': shop_info.get('country'),

                # 订单信息
                '订单编号': order_sn,  # 订单编号
                '下单时间': time_order,  # 生成时间， 时间戳 int
                '币种': currency,  # 交易货币，
                '实收金额': order_detail.get('total_amount'),  # 该订单的交易价格
            }

            row_order = base.append_row(ORDER_TABLE, row_data_order)
            row_id_order = row_order.get('_id')


            order_items = order_detail.get('items')
            if not order_items:
                continue
            item_image_list = []
            for order_item_detail in order_items:
                order_item_id = order_item_detail.get('item_id')
                item_detail = shop.get_item_detail(order_item_id)
                if not item_detail:
                    continue
                order_item_detail_item = item_detail.get('item')
                image_url = order_item_detail_item.get('images')[0]
                item_image_list.append(image_url)
                row_data_order_item = {
                    # 商品信息
                    '商品标题': order_item_detail.get('item_name'),  # 商品名称
                    '商品规格': order_item_detail.get('variation_name'),  # 商品细化标题
                    '商品折扣价': order_item_detail.get('variation_discounted_price'),  # 商品价格，折后
                    '商品单价': order_item_detail.get('variation_original_price'),     # 商品价格， 原价
                    '购买数量': order_item_detail.get('variation_quantity_purchased'),  # 商品购买数量

                    '商品图片': [image_url],
                    '商品链接': "https://%(country_abbr)s.xiapibuy.com/product/%(shop_id)s/%(item_id)s" % ({
                        'country_abbr': shop_info.get('country').lower(),
                        'shop_id':shop_info.get('shop_id'),
                        'item_id': order_item_detail.get('item_id')
                    })

                }
                row_order_item = base.append_row(ORDER_ITEM_TABLE, row_data_order_item)
                row_id_order_item = row_order_item.get('_id')
                row_order_item_link_id = base.get_column_link_id(ORDER_ITEM_TABLE, COL_LINK_ORDER)
                base.add_link(row_order_item_link_id,
                              ORDER_ITEM_TABLE,
                              ORDER_TABLE,
                              row_id_order_item,
                              row_id_order
                              )
            base.update_row(ORDER_TABLE, row_id_order, {
                "图片": item_image_list
            })

if __name__ == '__main__':
    test_partner_id = PARTNER_ID
    test_api_key = PARTNER_KEY

    # 测试用的shop_id限制
    shop_limits = SHOP_LIMITS
    n_days_before = N_DAYS_BEFORE
    shop_id_list = SHOP_ID_LIST

    api_token = context.api_token or "5b260eca2bb1ca2cab7787c148bb09ba343c9082"
    server_url = context.server_url or "http://127.0.0.1:8000/"


    base = Base(api_token, server_url)
    base.auth()

    insert_valid_infos_to_table(base, shop_limits, n_days_before, shop_id_list)
