
## 编程参考

SeaTable 中对象的数据结构:

* [数据结构](../data-structure.md)

SeaTable API 库介绍:

* [Base](base.md)
* [Query](query.md)
* [Rows](rows.md)
* [Links](links.md)
* [Columns](columns.md)
* [Constants](constants.md): 一些常量定义

Seatable API 使用说明

1. 授权 api(base.auth()) 是一个 async 函数, 需要在 async 函数中执行
2. 其他 api 都返回一个promise 对象 使用方法有两种
```
第一种:
base.listViews(tableName).then(views => {
  // 使用 views 完成需求
}).catch(error => {
  // 异常处理
})

第二种:

try {
  const views = await base.listViews(tableName);
  // 使用 views 完成需求
} catch (error) {
  // 异常处理
}
```

Seatable API Errors

* 400 Params invalid
* 403 Permission denied
* 413 exceed limit
* 500 Internal Server Error
