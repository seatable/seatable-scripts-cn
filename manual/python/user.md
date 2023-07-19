# Users

#### Get a user info

获取用户的信息， 通过用户的 ID 可以返回用户在 机构中的编号 (id_in_org) 以及姓名 (name)

```python
base.get_user_info（username）
```

其中

* username: 用户的 ID

##### 例子

```python
base.get_user_info("aea9e807bcfd4f3481d60294df74f6ee@auth.local")

# 返回
# {"id_in_org": "A0001", "name": "Tom"}
```

