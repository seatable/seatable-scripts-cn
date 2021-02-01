import requests
from seatable_api import context

"""
该脚本展示利用企业微信群组机器人进行表格中数据的发送。
"""
WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=39f5cb53-b909-4e30-9d99-75782"  # 建立群机器人之后自动生成的webhook地址，可以通过post请求该地址进行消息发送
HEADERS = {
    "Content-Type": "application/json"
}

COLUMNS =  ['customer_name', 'user_limit'] # 发送消息的列

# 构造发送文本消息的json数据结构
def json_text_msg(msg):
    return {
        "msgtype": "text",
        "text": {
            "content": msg,
        }
    }

# 格式化发送表格的消息
def format_msg(current_row, columns):
    '''
    current_row: 光标所在表格的行
    columns:  需要发送消息列
    '''
    return "\n".join(["%s: %s" % (column, current_row.get(column, '')) for column in columns])

def send_msg():
    current_row = context.current_row # 只能在表格脚本环境中运行
    msg = format_msg(current_row, COLUMNS)
    requests.post(url=WEBHOOK_URL, json=json_text_msg(msg), headers=HEADERS)


send_msg()