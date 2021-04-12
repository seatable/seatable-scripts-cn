import hashlib
import requests
import hmac
import time
import json
import re
from seatable_api import Base, context
BASE_URL_LIVE = "https://partner.shopeemobile.com"
BASE_URL_TEST_NEW = "https://partner.test-stable.shopeemobile.com"
BASE_URL_TEST_OLD = "https://partner.uat.shopeemobile.com"

PARTNER_ID = 843359
PARTNER_KEY = "004a04cf2f55f0f9a0dd22ca79a12ca69327011f2d3159125f75943e7f126b41"

SPLIT_PATERN = ",|，"
SHOP_LIMITS = 30 # 测试的店铺数量， 若要导入所有的授权店铺，设置为-1
N_DAYS_BEFORE = 7 # 测试多少天之前的订单，最高设置为 半个月之前 设置为 15
SHOP_ID_LIST = [] # 测试指定店铺数据

ORDER_ITEM_TABLE = "订单产品" # 订单产品表格名称
ORDER_TABLE = "订单"  # 订单表格名称
COL_LINK_ORDER = "订单链接"

class Shoppy(object):

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
            print("[ERROR: %s]" % res_dict)
            result = None
        else:
            result = res_dict
        return result

class ShopManager(object):

    def __init__(self, partner_id, partner_key):
        self.api = Shoppy(partner_id, partner_key)

    def get_shops_by_partner(self):
        return self.api.post('/api/v1/shop/get_partner_shop')



class Shop(object):



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
        order_basic_info_list = []
        for create_time_from, create_time_to in self.generate_time_interval(n_days_before):
            order_basic_info = self.api.post('/api/v1/orders/basics',
                             shopid=self.shop_id,
                             create_time_from=create_time_from,
                             create_time_to=create_time_to)
            order_basic_info_list.append(order_basic_info)
        return order_basic_info_list

    def generate_time_interval(self, n_days_before):
        # 处理一次请求只能间隔15天的情况
        time_now = int(time.time())
        time_interval_list = []
        one_day_timest = 24 * 3600
        n_days_before_tmp = n_days_before
        while n_days_before_tmp > 15:
            time_f = time_now - n_days_before_tmp * one_day_timest
            time_t = time_now - (n_days_before_tmp - 15) * one_day_timest
            time_interval_list.append((time_f, time_t)),
            n_days_before_tmp -= 15
        time_interval_list.append((time_now - n_days_before_tmp * 24 * 3600, time_now))
        return time_interval_list

    def generate_order_interval(self, order_sn_list):
        # 处理一次请求只能请求50个订单的情况
        # 数据结构， [[xxx,xxx,xxx...], [xxxx,xxx,xxx,....]]
        interval = 49
        tmp = 0
        order_sn_interval_list = []
        while tmp < len(order_sn_list):
            order_sn_interval_list.append(order_sn_list[tmp: tmp + interval])
            tmp += interval
        return order_sn_interval_list

    def get_order_detail(self, ordersn):
        return self.api.post('/api/v1/orders/detail',
                             shopid=self.shop_id,
                             ordersn_list = [ordersn,])

    def get_shop_order_details(self, n_days_before=14):
        order_list = [order_basic.get('orders') for order_basic in self.get_shop_orders(n_days_before)]
        ordersn_list = order_list and [o.get("ordersn") for o in sum(order_list, [])] or []
        if not ordersn_list:
            return None
        order_details_list = []
        for ordersn_interval in self.generate_order_interval(ordersn_list):
            order_details_list.append(self.api.post('/api/v1/orders/detail',
                             shopid=self.shop_id,
                             ordersn_list=ordersn_interval,
                            ))
        return order_details_list

    def get_item_detail(self, item_id):
        return self.api.post('/api/v1/item/get', shopid=self.shop_id, item_id=item_id)


    def get_escow_released_orders(self):
        create_time_to = int(time.time())
        create_time_from = create_time_to - 30 * 24 * 3600
        return self.api.post('/api/v2/orders/get_escrow_detail' , shopid=self.shop_id,
                             # release_time_from = create_time_from,
                             # release_time_to = create_time_to
                             )

class MoneyExchange(object):

    access_key = "b8ce91d3168c6d3588576d073f580cfd"

    def __init__(self):
        self.data_init()

    def data_init(self):
        self.get_exchange_rates_to_CNY()

    def get_exchange_rates_to_USD(self):
        url = "http://api.currencylayer.com/live?access_key=%s" % self.access_key
        resp = requests.get(url)
        resp_dict = resp.json()
        return resp_dict.get('quotes')

    def get_exchange_rates_to_CNY(self):
        exchange_rates_to_USD = self.get_exchange_rates_to_USD()
        USD_TO_CNY = exchange_rates_to_USD.get('USDCNY')
        d = {}
        for k, v in exchange_rates_to_USD.items():
            d[k] = v / USD_TO_CNY
        self.pool = d
        return d

    def get_exchange_rates_to_CNY_by_cur(self, currency='THB'):
        exchange_rates = self.pool

        return exchange_rates.get("USD%s" % currency)

    def exchange_to_CNY(self, money, currency='CNY'):
        exchange_rates = self.get_exchange_rates_to_CNY_by_cur(currency)
        money_exchange = money / exchange_rates
        return float("%.2f" % money_exchange)


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


def format_order_escow_infos(order_escow_infos):
    """
    {":ordersn":":releasetime"}
    :param orderinfos:
    :return:
    """
    return {info.get('ordersn'): info.get('escow_release_time') for info in order_escow_infos}


def currency_exchange_rate(escow_release_timestamp, from_c=None, to_c='RMB'):
    pass

def parse_order_status(order_status):
    # 将订单状态转换为中文
    "ALL/UNPAID/READY_TO_SHIP/COMPLETED/IN_CANCEL/CANCELLED/TO_RETURN"
    return {
        "UNPAID": '待付款',
        "READY_TO_SHIP": "待发运",
        "SHIPPED": "已发运",
        "COMPLETED": "已完成",
        "IN_CANCEL": "取消中",
        "CANCELLED": "已取消",
        "TO_RETURN": "退款 / 退货",
        "RETRY_SHIP":"再次发货",
        "TO_CONFIRM_RECEIVE": "待确认收货"
    }.get(order_status)

def order_id_row_id_map(base):
    # 构造订单编号和行号的映射, 用于更新表格
    """
    {
    ": order_id": ":row_id"
    ": order_id2": ":row_id2"
    ": order_id3": ":row_id3"
    }
    """
    return {
        row.get('订单编号') : row.get('_id') for row in base.list_rows(ORDER_TABLE)
    }

def order_key_list(base, operation="row_create"):
    # 通过摘取订单表中的一些信息来做唯一的索引
    # 构造索引数据结构和上述唯一索引做比较， 如果不匹配， 则执行创建行或更新行的逻辑
    if operation not in ["row_create", "row_update"]:
        raise ValueError('Row operation invalid, please select row_create or row update')

    # 创建行， 使用订单编号, 创建时间来做唯一索引
    if operation == 'row_create':
        return [(
            row.get('订单编号'),
            row.get('店铺编号'),
        )
        for row in base.list_rows(ORDER_TABLE)
        ]

    # 更新行， 使用编号， 时间， 回款金额，订单状态来做唯一索引
    if operation == 'row_update':
        return [(
            row.get('订单编号'),
            row.get('店铺编号'),
            str(row.get('回款金额')),
            row.get('订单状态')

        ) for row in base.list_rows(ORDER_TABLE)]


def get_domain_by_country(country):
    """
    TW：https://seller.xiapi.shopee.cn/account/signin
    MY：https://seller.my.shopee.cn/account/signin
    SG：https://seller.sg.shopee.cn/account/signin
    ID：https://seller.id.shopee.cn/account/signin
    TH：https://seller.th.shopee.cn/account/signin
    VN:  https://seller.vn.shopee.cn/account/signin
    PH：https://seller.ph.shopee.cn/account/signin
    BR:  https://seller.br.shopee.cn/account/signin
    :param country:
    :return:
    """
    return {
        "TW": "xiapi",
        "MY": "my",
        "SG": "sg",
        "ID": "id",
        "TH": "th",
        "VN": "vn",
        "PH": "ph",
        "BR": "br"
    }.get(country)


# 添加行API
def sync_infos_from_shopee(base, shop_limits=2, n_days_before=2, shop_id_list = None, money_exchanger=None, ship_cost_default=3):
    valid_info_list = []
    # 按照授权店铺-->具体店铺-->店铺订单-->订单项商品的不同level层级深入
    order_key_list_create = order_key_list(base, operation='row_create')
    order_key_list_update = order_key_list(base, operation='row_update')
    order_row_map = order_id_row_id_map(base)

    # level 0: 授权店铺
    if shop_id_list:
        shop_ids = shop_id_list
    else:
        shop_ids = _get_authed_shop_id(shop_limits)
    order_create_count, order_update_count = 0, 0
    for shop_id in shop_ids:

        shop = Shop(test_partner_id, test_api_key, shop_id)
        shop_info = shop.get_shop_info()
        #根据excel表构造字段
        if not shop_info:
            continue

        # level 2: 店铺中订单信息, 包括订单编号， 币种， 下单时间
        orders_detail_list = shop.get_shop_order_details(n_days_before=n_days_before)
        if not orders_detail_list:
            continue
        order_details = [orders.get('orders') for orders in orders_detail_list]
        for order_detail in sum(order_details, []):
            order_sn = order_detail.get('ordersn')
            currency = order_detail.get('currency')
            time_order = timestamp2str(order_detail.get('create_time'))
            total_amount = order_detail.get('total_amount')
            escow_amount = order_detail.get('escrow_amount')
            order_status = parse_order_status(order_detail.get('order_status'))
            if (order_sn, shop_id) in order_key_list_create:
                #如果订单已经存在， 看订单是否需要更新
                if (order_sn, shop_id, escow_amount, order_status) in order_key_list_update:
                    # 如果字段都匹配， 跳过
                    print("[PASS] order_sn %s exists" % order_sn)
                    continue
                else:
                    # 执行订单更新逻辑
                    row_data_order_update = {
                        "订单状态": order_status,
                        "回款金额": escow_amount
                    }
                    row_id = order_row_map.get(order_sn)
                    base.update_row(ORDER_TABLE, row_id, row_data_order_update)
                    order_update_count += 1
                    print("[ORDER UPDATED][%s]: 状态: %s / 回款金额: %s" % (order_sn, order_status, escow_amount))

            else:
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
                    '实收金额': total_amount,  # 该订单的交易价格
                    '实收金额RMB': money_exchanger.exchange_to_CNY(float(total_amount),currency),  # 该订单的交易价格
                    '回款金额': escow_amount, # 订单的回款金额， 实收金额-佣金-平台手续费
                    '回款金额RMB':money_exchanger.exchange_to_CNY(float(total_amount),currency),  # 该订单的回款金额
                    '订单状态': order_status,
                    '货代运费RMB': ship_cost_default, # 货代运费， 给一个初始默认值
                }

                row_order = base.append_row(ORDER_TABLE, row_data_order)
                row_id_order = row_order.get('_id')
                order_create_count += 1
                print("[ORDER CREATED][%s]" % order_sn)

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
                    original_price = order_item_detail.get('variation_original_price')
                    row_data_order_item = {
                        # 商品信息
                        '商品标题': order_item_detail.get('item_name'),  # 商品名称
                        '商品规格': order_item_detail.get('variation_name'),  # 商品细化标题
                        '商品折扣价': order_item_detail.get('variation_discounted_price'),  # 商品价格，折后
                        '商品单价': original_price,     # 商品价格， 原价
                        '商品单价RMB': money_exchanger.exchange_to_CNY(float(original_price), currency),   # 商品价格， 原价
                        '购买数量': order_item_detail.get('variation_quantity_purchased'),  # 商品购买数量

                        '商品图片': [image_url],
                        '商品链接': "https://%(country_abbr)s.xiapibuy.com/product/%(shop_id)s/%(item_id)s" % ({
                            'country_abbr': get_domain_by_country(shop_info.get('country')),
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

    sync_info_msg = "新增订单个数: %s / 更新订单个数: %s" % (order_create_count, order_update_count)
    return sync_info_msg


if __name__ == '__main__':
    test_partner_id = PARTNER_ID
    test_api_key = PARTNER_KEY
    test_shop_id = 250963379

    # 测试用的shop_id限制
    shop_limits = SHOP_LIMITS
    n_days_before = N_DAYS_BEFORE
    shop_id_list = SHOP_ID_LIST
    me = MoneyExchange()


    # 1. 获取客户信息表
    customer_info_table_api_token = "624ab6fe4e1fabbf7d7f2a975875065420083be3"
    cloud_server_url = "https://cloud.seatable.cn/"

    base_customer_info = Base(customer_info_table_api_token, cloud_server_url)
    base_customer_info.auth()
    for row in base_customer_info.list_rows('客户信息'):
        shop_ids = row.get('店铺ID')

        if not shop_ids:
            shop_id_list = []
        else:
            shop_id_list = [int(shop_id_str.strip()) for shop_id_str in re.split(SPLIT_PATERN, shop_ids)]
        base_token = row.get('Base Token(管理员生成)')
        if not base_token:
            continue
        try:
            n_days_before = int(row.get('数据导入天数(<15)'))
        except:
            n_days_before = 7
        try:
            ship_cost_default = int(row.get('货代运费RMB默认'))
        except:
            ship_cost_default = 3

        customer_name = row.get('用户名')
        try:
            customer_base = Base(base_token, cloud_server_url)
            customer_base.auth()
        except Exception as e:
            print("[ERROR] Base %s auth faild" % base_token)
            continue

        sysn_info_msg = sync_infos_from_shopee(
            customer_base,    # 客户base
            shop_limits,      # 测试shop的数量， 正式使用时设置为-1
            n_days_before,    # 倒入n天前订单
            shop_id_list,     # 客户的shop_id, 为空导入所有订单, 用于管理员
            money_exchanger=me,  # 汇率转换器
            ship_cost_default=ship_cost_default, # 货代运费默认值
        )

        print("客户数据同步结果: [%s] %s" % (customer_name, sysn_info_msg))

