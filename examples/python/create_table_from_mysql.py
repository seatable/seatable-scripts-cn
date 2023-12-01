from seatable_api.constants import ColumnTypes
from seatable_api import Base, context
from sqlalchemy import create_engine

TABLE_NAME = 'Table_1'
SERVER_URL = context.server_url or 'https://cloud.seatable.cn/'
API_TOKEN = context.api_token  or 'cacc42497886e4d0aa8ac0531bdcccb1c93bd0f5'


class DBConnection():
    def __init__(self, db_instance):
        self.db_engine = create_engine("mysql+mysqlconnector://username:password@localhost:8002/{}?charset=utf8mb4".format(db_instance))
        self.db_engine.connect()

    def read(self, sql): #返回[{}]
        """Executes a read query and returns a list of dicts, whose keys are column names."""
        ret = self.db_engine.execute(sql).fetchall()
        # return list of dict instead of tuple
        if ret is not None:
            return [{key: value for key, value in row.items()} for row in ret if row is not None]
        else:
            return [{}]  

    def write(self,sql):
        return
    

class Seatable:

    def __init__(self):
        """初始化登录接口
        """
        self.base = Base(API_TOKEN, SERVER_URL)
        self.base.auth()


    def create_cols(self,dbname,sql):
        """创建表头（非必需）
        """
        conn = DBConnection(dbname)
        # describe 表属性来建seatable表头
        mysql_data = conn.read(sql)
        try:
            for data in mysql_data:
                # 默认都插入text类型，有需要可以自己根据field字段配置
                self.base.insert_column(TABLE_NAME, data['Field'], ColumnTypes.TEXT )
            return 'success'
        except:
            return 'fail'
        
if __name__ == "__main__":
    s = Seatable()
    DB = 'DB'
    sql = 'describe tables;'
    s.create_cols(DB,sql)