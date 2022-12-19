

## 提交工作流任务

以当前用户提交一个工作流任务。


#### Add workflow task with a new row

使用一个新行，提交一个工作流任务


```python
base.add_workflow_task(workflow_token, row_data, link_rows=None, new_linked_rows=None)
```

##### 例子

```python
base.add_workflow_task('4d703526-bcd1-4a9c-a234-fe9671766672', {"name": "new workflow task"})
```

#### Add workflow task with an existed row

使用已存在的行添加工作流任务

```python
base.add_workflow_task_with_existed_row(workflow_token, row_id)
```

##### 例子

```python
base.add_workflow_task_with_existed_row('4d703526-bcd1-4a9c-a234-fe9671766672', 'TbxyQfDXTR6EQcyZ4OxB7w')
```
