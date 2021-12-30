from seatable_api import Base, context
import time
import hashlib
import requests

SERVER_URL = context.server_url or "https://cloud.seatable.cn/"
API_TOKEN = context.api_token or "fda91163dc4e67d3f854c2413d9cb21dc1973e92"


APP_KEY = "xxxxxx"
SRC_KEY = "xxxxxx"
ts = int(round(time.time() * 1000))

# 通过md5加密算法用APP_KEY 和 SECRET_KEY生成签名
str_conc = "%s%s%s" % (APP_KEY, ts, SRC_KEY)
m = hashlib.md5(str_conc.encode())
sign = m.hexdigest()


headers = {
        'Auth-Version': "2.0",
        'appkey': APP_KEY,
        'timestamp': str(ts),
        'sign': sign,
    }

COMPANY_TABLE = "公司"
FINACIAL_TABLE = "融资信息"
ORG_CODE_COLUMN = "统一信用代码"
LINK_COLUMN = "融资信息"

# 用api通过企业信用代码进行请求返回融资信息, org_code： 公司信用代码
def get_data_by_org_code(org_code):
    data = {"name": org_code}
    url = "https://api.qixin.com/APIService/v2/financing/getFinancingByName"
    response = requests.request("GET", url, params=data, headers=headers)
    return response.json().get('data', {})


def get_table_id_by_name(base, table_name):
    metadata = base.get_metadata()
    for t in metadata.get('tables', {}):
        if t.get('name') == table_name:
            return t.get('_id')

    return None

def load_finance_data_keys(base, org_codes=None):
    key_list = []
    org_code_row_ids_map = {}
    for row in base.list_rows(FINACIAL_TABLE):
        org_code = row.get("统一信用代码")
        if org_codes and org_code not in org_codes:
            continue
        finance_count = row.get("融资轮次")
        finance_date = row.get('融资日期')
        finance_amount = row.get('融资金额')
        key_list.append("%s-%s-%s-%s" % (org_code, finance_count, finance_date, finance_amount))

        org_row_id_list = org_code_row_ids_map.get(org_code, []) or []
        org_row_id_list.append(row.get('_id'))
        org_code_row_ids_map[org_code] = org_row_id_list

    return key_list, org_code_row_ids_map


def run(org_codes=None, make_links=None):
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()

    link_column_id = base.get_column_link_id(COMPANY_TABLE, LINK_COLUMN)
    company_table_id = get_table_id_by_name(base, COMPANY_TABLE)
    finacial_table_id = get_table_id_by_name(base, FINACIAL_TABLE)
    finacial_table_row_keys, org_row_ids_map = load_finance_data_keys(base, org_codes)

    for row in base.list_rows(COMPANY_TABLE):
        org_code = row.get(ORG_CODE_COLUMN)
        if not org_code:
            continue

        if org_codes and org_code not in org_codes:
            continue

        # 如果已有链接， 跳过
        total_data = get_data_by_org_code(org_code)
        finacial_data_list = total_data.get('financing_list', [])
        if not finacial_data_list:
            continue
        company_row_id = row.get('_id')

        finance_row_id_list = org_row_ids_map.get(org_code, []) or []
        for finance_data in finacial_data_list:

            # 融资轮次
            finance_count = finance_data.get('financing_round')
            # 融资日期
            finance_date = finance_data.get('finance_date')
            # 融资金额
            finance_amount = finance_data.get('financing_amount')
            # 投资机构名称
            row_key = "%s-%s-%s-%s" % (org_code, finance_count, finance_date, finance_amount)
            if row_key in finacial_table_row_keys:
                continue
            org_list = finance_data.get('investors', [])
            if org_list:
                orgs = ", ".join([inv.get('org_name', '') for inv in org_list])
            else:
                orgs = ""

            # 融资新闻URL
            news_list = finance_data.get('news', [])
            if news_list:
                news_url = news_list[0].get('url', '')
            else:
                news_url = ''

            # 插入行
            finance_row = base.append_row(FINACIAL_TABLE, {
                "融资轮次": finance_count,
                "融资日期": finance_date,
                "融资金额": finance_amount,
                "投资机构名称": orgs,
                "融资新闻URL": news_url,
                "统一信用代码": org_code
            })

            finance_row_id_list.append(finance_row.get('_id'))
        if not finance_row_id_list:
            continue
        if make_links:
            # 批量更新链接列
            base.batch_update_links(
                link_column_id,
                company_table_id,
                finacial_table_id,
                [company_row_id, ],
                {company_row_id: list(set(finance_row_id_list))}
            )

if __name__ == '__main__':
    run()
