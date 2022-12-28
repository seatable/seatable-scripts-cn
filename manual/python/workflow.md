

## 提交工作流任务

提交一个工作流任务，可以指定发起人。


#### Add workflow task with a new row

使用一个新行，提交一个工作流任务


```python
base.add_workflow_task(workflow_token, row_data, initiator=None, link_rows=None, new_linked_rows=None)

# initiator: 发起人
# link_rows: 对应于表单中链接列 "链接已有记录" 功能，用于链接已有记录
# new_linked_rows: 对应于表单中链接列 “增加新记录" 功能，用于往链接的表中增加新的记录项，并建立链接关系

```

##### 例子

```python
base.add_workflow_task("4d703526-bcd1-4a9c-a234-fe9671766672", {"name": "new workflow task"})

# 指定发起人
base.add_workflow_task("4d703526-bcd1-4a9c-a234-fe9671766672", {"name": "new workflow task"}, initiator='aa59ffc39fc8487e9e973507dc642e77@auth.local')

# 更新链接列
base.add_workflow_task(
    '4d703526-bcd1-4a9c-a234-fe9671766672',
    {"name": "new workflow task"},
    linked_rows=[{
        "link_id": "os6S",
        "other_table_name": "Table2",
        "row_ids": ["Kkk8lg_xSouJnIJ4BxRFQA", "BaSaENBQT-mKlGAqeAdiFA"]
    }],
    new_linked_rows=[{
        "link_id": "os6S",
        "other_table_name": "Table2",
        "row_datas": [
            {"name": "new link 1"},
            {"name": "new link 2"}
        ]
    }]
)
```

#### Add workflow task with an existed row

使用已存在的行添加工作流任务

```python
base.add_workflow_task_with_existed_row(workflow_token, row_id, initiator=None)
```

##### 例子

```python
base.add_workflow_task_with_existed_row("4d703526-bcd1-4a9c-a234-fe9671766672", "TbxyQfDXTR6EQcyZ4OxB7w")

base.add_workflow_task_with_existed_row("4d703526-bcd1-4a9c-a234-fe9671766672", "TbxyQfDXTR6EQcyZ4OxB7w", initiator="aa59ffc39fc8487e9e973507dc642e77@auth.local")
```
