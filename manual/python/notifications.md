# Notifications

#### Send toast notifications

给用户发出一个弹出的通知

```python
base.send_toast_notification(username, msg, toast_type='success')
```

其中

* username: 用户的 ID
* msg: 通知消息内容
* toast_type: 通知的类型，支持 "success", "warning", "danger"

##### 例子

```python
base.send_toast_notification(
"aea9e807bcfd4f3481d60294df74f6ee@auth.local",
  "error request",
  "danger"
)
```
