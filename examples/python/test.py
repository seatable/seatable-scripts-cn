from seatable_api import Base
API_TOKEN = "3e53efce0b691c93a3e53364c244708804853e05"
SERVER_URL = "http://127.0.0.1:8000/"

table_name = "基本信息"

base = Base(API_TOKEN, SERVER_URL)
base.auth()
filters = [{
    "column_name":"姓名",
    "filter_predicate":"contains",
    "filter_term":"灰太狼"
}]
print(base.filter_rows(table_name, view_name=None, filters=filters, filter_conjunction='And'))