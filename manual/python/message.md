# Message

通过在 Base 中设置的第三方账号信息可以进行消息发送。包括邮件发送和企业微信群组发送。

## 第三方账号信息认证

### 1.base 初始化认证

```python
base.auth(msg_sender_account="xxxx")
```

其中

* msg_sender_account: base 中设置的第三方账户的 account_name

例子如下

```python
base.auth(msg_sender_account="My email server")
```

### 2. 发送消息时进行认证

这个可以使得在发送多条消息的时候，中途切换第三方账号

```
base.send_email(msg, using_account="xxxx", **kwargs)
base.send_wechat_msg(msg, using_account="xxxx")
```

其中

* msg: 发送的消息主体内容；
* using_account: base 中设置的第三方账户的 account_name;

## 消息发送

以下通过对两种认证方式的消息发送进行举例

### 微信发送

```python
# 方式1:
base = Base(....)
base.auth(msg_sender_account="My wechat account")
base.send_wechat_msg("您好， 我是该群微信管理员")

# 方式2:
base.send_wecaht_msg("您好， 我是该群微信管理员", using_account="My wechat account")
```

### 邮件发送

邮件发送机制中需要建立 smtp 的链接， 这个比较耗时(5秒左右)，因此，我们在进行账号认证的时候，就把该连接进行建立，然后可以用此连接进行邮件发送.

```python
base.send_email(msg, using_account=None, **kwargs)
```

其中

 kwargs: 其他参数：
  * send_to (必填)：接收方的邮件，可以是列表包含多个邮件。
  * subject  (必填)： 邮件主题
  * from：发件人, 如果未设置，默认邮箱服务器的 host_user
  * copy_to: 抄送方邮件， 可以是列表包含多个邮件
  * reply_to: 回复邮件
  * quit_after_send: True 或者 False， 默认是 False。 发送完成之后是否关闭与服务器的链接。

#### 初始化认证

```python
base = Base(....)
base.auth(msg_sender_account="My email account")

base.send_email(
	"您好，请查收邮件",
  subject="Test",
  send_to=['350178982@qq.com',"r350178982@126.com"],
  copy_to='jiwei_ran@sina.com'
)
```

#### 不同邮件账号发送中认证

例如使用 “My email account1” 和 “My email account2” 分别进行邮件发送。

```python
base.send_email(
	"user1 您好",
  using_account="My email account1"
  subject="Test1",
  send_to=['user1@qq.com',"user1@126.com"],
  copy_to='jiwei_ran@sina.com'
)

base.send_email(
	"user2 您好",
  using_account="My email account2",
  subject="Test2",
  send_to=['user2@qq.com',"user2@126.com"],
  copy_to='jiwei_ran@sina.com'
)
```

#### 同一邮件账号发送中认证

若只使用同一个邮件账号,如 “My email account”， 只需要在发送的第一次进行认证，传递 using_account 参数即可

```python
base.send_email(
	"user1 您好",
  using_account="My email account"
  subject="Test1",
  send_to=['user1@qq.com',"user1@126.com"],
  copy_to='jiwei_ran@sina.com'
)
base.send_email(
	"user2 您好",
  subject="Test2",
  send_to=['user2@qq.com',"user2@126.com"],
  copy_to='jiwei_ran@sina.com'
)

base.send_email(...)
.....
```

#### 切断发送连接

一般在邮件发送完成之后需要切断 smtp 连接, 同样有两种方式

```python
# 方式1 
base.msq_quit()

# 方式2 发送完最后一条消息之后传递 quit_after_send 参数
base.send_email(
	....,
  quit_after_send=True
)
```



