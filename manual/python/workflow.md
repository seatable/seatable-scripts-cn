

## 提交工作流任务

提交一个工作流任务，可以指定发起人。


#### Add workflow task with a new row

使用一个新行，提交一个工作流任务


```python
base.add_workflow_task(workflow_token, row_data, initiator=None, link_rows=None, new_linked_rows=None)
```

##### 例子

```python
base.add_workflow_task('4d703526-bcd1-4a9c-a234-fe9671766672', {"name": "new workflow task"})
base.add_workflow_task('4d703526-bcd1-4a9c-a234-fe9671766672', {"name": "new workflow task"}, initiator='aa59ffc39fc8487e9e973507dc642e77@auth.local')
```

#### Add workflow task with an existed row

使用已存在的行添加工作流任务

```python
base.add_workflow_task_with_existed_row(workflow_token, row_id, initiator=None)
```

##### 例子

```python
base.add_workflow_task_with_existed_row('4d703526-bcd1-4a9c-a234-fe9671766672', 'TbxyQfDXTR6EQcyZ4OxB7w')
base.add_workflow_task_with_existed_row('4d703526-bcd1-4a9c-a234-fe9671766672', 'TbxyQfDXTR6EQcyZ4OxB7w', initiator='aa59ffc39fc8487e9e973507dc642e77@auth.local'))
```
