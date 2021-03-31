# Message

### 微信发送

```python
base.send_wechat_msg(account_name, msg)
```

其中

* account_name： 第三方账户名称
* msg： 消息主体

**例子**

```python
base.send_wechat_msg("My wechat group", "您好， 我是管理员， 请多关照！")
```



### 邮件发送

```python
base.send_email(account_name, msg, **kwargs)
```

其中

* account_name: 第三方账户名称
* msg：消息主体

* kwargs: 其他参数：
    * send_to (必填)：接收方的邮件，可以是列表包含多个邮件。
    * subject  (必填)： 邮件主题
    * from：发件人, 如果未设置，默认邮箱服务器的 host_user
    * copy_to: 抄送方邮件， 可以是列表包含多个邮件
    * reply_to: 回复邮件

**例子**

```python
base.send_email(
 	"My email account",
	"您好，请查收邮件",
  subject="Test",
  send_to=['350178982@qq.com',"r350178982@126.com"],
  copy_to='jiwei_ran@sina.com'
)
```

