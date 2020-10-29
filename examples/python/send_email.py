import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from urllib import parse

import requests
from seatable_api import Base, context


server_url = context.server_url
api_token = context.api_token

base = Base(api_token, server_url)

base.auth()


#设置smtplib所需的参数

#下面的发件人，收件人是用于邮件传输的。

smtpserver = 'smtp.163.com'
username = '13069744444@163.com'
password='PAXBERVGCMPKGIJJ'
sender='13069744444@163.com'


#收件人为多个收件人
#可以指定邮箱
receivers=['1223408888@qq.com']

#如果想用表格中的收件箱例如
#有一张表名字为联系人 有一个邮箱列 存放邮箱地址

receiver_rows = base.list_rows('联系人')
receivers = [row['邮箱'] for row in receiver_rows if row.get('邮箱')]
subject = 'SeaTable邮件发送'

#通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
#subject = '中文标题'
#subject=Header(subject, 'utf-8').encode()

#构造邮件对象MIMEMultipart对象
#下面的主题，发件人，收件人，日期是显示在邮件页面上的。

msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = '13069744444@163.com <13069744444@163.com>'

#msg['To'] = 'XXX@126.com'

#收件人为多个收件人,通过join将列表转换为以;为间隔的字符串

msg['To'] = ";".join(receivers) 

#构造文字内容

# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"
# text_plain = MIMEText(text,'plain', 'utf-8')
# msg.attach(text_plain)


#构造html
#如果你想从SeaTable中读取文件作为正文，请参阅SeaTable脚本编程手册的获取下载链接

html = """
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       这是一封来自
       SeaTable样例的邮件
    </p>
  </body>
</html>
"""

text_html = MIMEText(html,'html', 'utf-8')
msg.attach(text_html)

#构造附件，从SeaTable中读取文件构造附件，只是举例，请按需更改

rows = base.list_rows('Table3')
filename = rows[0]['文件'][0]['name']
file_url = rows[0]['文件'][0]['url']  # 获取文件url
path = file_url[file_url.find('/files/'):]
download_link = base.get_file_download_link(parse.unquote(path))  # 获取文件下载链接

try:
    response = requests.get(download_link)
    if response.status_code != 200:
        print('下载图片失败, status code: ', response.status_code)
        exit(1)
except Exception as e:
    print(e)
    exit(1)

text_att = MIMEText(response.content, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
text_att["Content-Disposition"] = 'attachment;filename*=UTF-8\'\'' + parse.quote(filename)

msg.attach(text_att)

#发送邮件

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')

#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# smtp.set_debuglevel(1)

smtp.login(username, password)
smtp.sendmail(sender, receivers, msg.as_string())
smtp.quit()
