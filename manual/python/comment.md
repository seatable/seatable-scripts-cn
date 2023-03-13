# 行评论

以下的方法可以对 Base 内评论进行操作

**使用评论相关 API 时请先调用 Base.auth_as_user(login, password) 方法进行用户登录**

#### Add a comment

对某行评论

```python
base.add_comment(table_id, row_id, comment)
```

##### 例子

```python
table_id = '0000'
row_id = 'IN6FfRQLR9GAYX-6VHPvvA'
comment = 'comment from seatable-api'

base.add_comment(table_id, row_id, comment)
```

返回

```Python
{'success': True}
```

#### Get the count number of a row's comments

获取某行评论数量

```python
base.get_comments_count(row_id)
```

返回为一个数字

#### Get comments of a row

获取某行评论，支持分页

```Python
base.get_comments(row_id, page=1, per_page=25)
```

返回

```Python
{
    "comment_list": [
        {
            'id': 1,
            'author': '27e19630f2044e1abe9e86e17e4c8418@auth.local',
            'comment': 'comment content',
            'created_at': '2023-03-10T16:09:30+00:00',
            'updated_at': '2023-03-10T16:09:30+00:00',
            'dtable_uuid': '281bb8dc19fb4257ad5feabccc8a9333',
            'row_id': 'R6anZyjkRJK-HGrqkLvVsA',
            'detail': None,
            'resolved': False
        }
    ],
    "count": 1
}
```

#### Resolve a comment

将评论置为已解决

```Python
base.resolve_comment(comment_id)
```

返回

```Python
{'success': True}
```

#### Delete a comment

删除评论

```Python
base.delete_comment(comment_id)
```

返回

```Python
{'success': True}
```

#### Get comments of a base within days

获取 Base 几天内的评论，不止某一行

```Python
base.get_comments_within_days(days)
```

返回

```Python
[
    {
        'id': 1,
        'author': '27e19630f2044e1abe9e86e17e4c8418@auth.local',
        'comment': 'comment content',
        'created_at': '2023-03-10T16:09:30+00:00',
        'updated_at': '2023-03-10T16:09:30+00:00',
        'dtable_uuid': '281bb8dc19fb4257ad5feabccc8a9333',
        'row_id': 'R6anZyjkRJK-HGrqkLvVsA',
        'detail': None,
        'resolved': False
    },
    {
        'id': 3,
        'author': '27e19630f2044e1abe9e86e17e4c8418@auth.local',
        'comment': 'comment content on another row',
        'created_at': '2023-03-10T16:09:30+00:00',
        'updated_at': '2023-03-10T16:09:30+00:00',
        'dtable_uuid': '281bb8dc19fb4257ad5feabccc8a9333',
        'row_id': 'Vwnx6xEFS6qjgbhZAUNM7Q',
        'detail': None,
        'resolved': True
    }
]
```
