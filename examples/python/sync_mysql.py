import pymysql
from seatable_api import Base, context

# Base config
SERVER_URL = context.server_url or  'http://127.0.0.1:8000'
API_TOKEN = context.api_token or '48b6a41a0c2e1ee4bf294ed42445914025a0a60c'

# Table config
TABLE_NAME = 'Table1'
NAME_COLUMN = 'Name'

# Mysql config
HOST = 'localhost'
USER = ''
PASSWORD = ''
DB = 'seatable'

def sync_mysql():
    """Sync database into the table
    """
    # base initiated and authed
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()

    rows = base.list_rows(TABLE_NAME)
    row_keys = [row.get(NAME_COLUMN) for row in rows]

    # mysql data
    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB)

    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM order"
        cursor.execute(sql)
        mysql_data = cursor.fetchall()

    # sync
    for item in mysql_data:
        if item.get('name') not in row_keys:
            row_data = {
                'Name': item.get('name'),
            }
            base.append_row(TABLE_NAME, row_data)


if __name__ == '__main__':
    sync_mysql()