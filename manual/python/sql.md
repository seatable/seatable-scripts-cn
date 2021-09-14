# SQL 支持

SeaTable 中数据查询支持 SQL 语句。使用 SQL 语句会检索完整的数据集，也就是包括归档和非归档的数据。

## 语法

目前只支持基本的 select 语句，语法如下：

```
SELECT [DISTINCT] fields FROM table_name [WhereClause] [OrderByClause] [GroupByClause] [Limit Option]
```

说明：

* 暂不支持多个子表查询的 `JOIN` 语句;
* where 语句中支持大部分的表达式 (算数表达式， 比较表达式等), 关键字包括： `[NOT] LIKE`, `IN`, `BETWEEN ... AND ...`, `AND`, `OR`, `NOT`, `IS [NOT] TRUE`, `IS [NOT] NULL`. 其中：
  * 算术表达式只支持数字.
  * `LIKE` 语句只支持字符串.
  * `BETWEEN ... AND ...` 语句只支持数字与时间. 其中时间常数应该是 ISO 格式的字符串 (如:  "2020-09-08 00:11:23");
* `GROUP BY` 语法比较严格. 除了聚合函数的关键字(`COUNT`, `SUM`, `MAX`, `MIN`, `AVG`) 以及公式的关键字(细节请查看本文档的扩展语法)之外，所选字段也必须同样也要出现在 group by 的语句中;
* "order by" 语句表示根据某字段排序， 该字段必须出现在 select 表达式中。比如：`select a from table order by b`是无效语句; 而 `select a from table order by a` 或者 `select abs(a), b from table order by abs(a)` 则可以运行；
* Limit 语句和 MySQL 格式一样，语法是 `OFFSET ... LIMIT ...`。

查询结果是以 JSON 的格式进行返回. 其中 key 字段是列的唯一标示， 而不是列名。

## 数据类型

以下表格列出了 SeaTable 表格中的数据与 SQL 语句字段中数据类型的对应情况

| SeaTable 数据类型 | SQL 字段类型                                                 |
| :---------------- | :----------------------------------------------------------- |
| 文本              | String                                                       |
| 长文本            | String                                                       |
| 数字              | Float                                                        |
| 单选              | String.  在 where 表达式中， 需要使用选项的名称，如：`where single_select = "New York"` , 而在查询结果中， 该字段返回的是选项的 key 而非名称， 如果需要在 UI 上进行查询结果展示， 需要把这个 key 转化成名称 |
| 多选              | 包含 string 的列表. 在 where 表达式中， 需要使用选项的名称，如：`where single_select = "New York"` , 而在查询结果中， 该字段返回的是选项的 key 而非名称， 如果需要在 UI 上进行查询结果展示， 需要把这个 key 转化成名称 |
| 勾选              | Bool                                                         |
| 日期              | Datetime. ISO 格式的时间字符串 如:  "2006-1-2" or “2006-1-2 15:04:05“. |
| 图片              | 包含图片的 URL 的列表                                        |
| 文件              | 不能用于 where 语句， 查询结果将以 JSON 的格式进行返回。     |
| 协作人            | 包含用户 ID 的列表, 格式如 5758ecdce3e741ad81293a304b6d3388@auth.local, 如果用到用户名称，需要通过 SeaTable 的相关 API 进行转换。 |
| 链接其他记录      | 不能用于 where 语句， 被查询时，以包含行 ID 的列表的形式返回， 其中会返回以创建时间排序的前10行。 |
| 公式              | 数据类型根据通过该公式计算得到的返回值类型而定               |
| 创建者            | 用户 ID, string                                              |
| 创建时间          | Datetime                                                     |
| 修改者            | 用户 ID, string                                              |
| 修改时间          | Datetime                                                     |
| 自动序号          | String                                                       |
| URL               | String                                                       |
| 邮箱              | String                                                       |
| duration          | Float                                                        |

此外， 在 where 语句中， 如果一个列中的数据是列表类型呈现(如协作人，多选列等)， 并且该列与一个字符串做比较时， 如果该字符串在该列表中时， 则会判断为 true 并且返回结果。 如：`SELECT * FROM tb3 where multi_select ='select 1' and multi_select='select 2'` , 如果列 multi-select 中同时包含 ’select 1’ 和 ‘select 2’， 则满足查询条件并返回。

## 扩展语法

### SQL 查询中使用公式

 SeaTable 中的一些公式也可以用于 SQL 查询当中， 以下有几点说明：

* 链接公式暂不支持， 如 {link.age}, 这种查询无效;
* 查询的列名不支持使用大括号(“{}”)来修饰， 如：`select abs({column}) from talbe;` 属于无效查询， 应该写成：`select abs(column) from table;` ，此规则同 SQL 语法一致;
* 如果字段名称中包含空格或连接符“-”， 可是使用左引号("\`\`")来进行修饰， 如: select abs \`column-a\` from table;
* 不支持给子段起别名， 如：`select abs(t.column) from table as t;` 为无效查询；
* 公式可以用在 group by 以及 order by 表达语句当中;

额外支持的公式函数:

* `STARTOFWEEK(date, weekStart)`: 返回包含 “date” 的星期的第一天的日期， “weekstart” 可选 “sunday” 或者 “monday” 来作为一周的第一天
* `Quarter(date)`: 返回第几个季度，包括1，2，3，4.
* `ISODate(date)`: 返回 ISO 格式的日期， 如: "2020-09-08"
* `ISOMonth(date)`: 返回 ISO 格式的月份， 如: "07"

以上的公式可以用于 group by 分组， 按星期， 月，季度，  日期等， 如：`select sum(sale) from SalesRecord group by ISODate(SalesTime)` , 返回每天的总销量。

更多支持的公式函数请参考\[./function.md]。

### 查询字符串列表

协作人以及多选类型以字符串列表的方式进行呈现， SeaTable 从 UI 层面上对这过滤两种类型的数据使用特别的函数呈现， 包括`HAS ANY OF`, `HAS ALL OF`, `HAS NONE OF`, `IS EXACTLY`.  这些关键字同样也适用于 SQL 查询语法中。比如：名为 “city” 的列属于多选类型， 我们想查询出所有包含 “New York” 和  “Paris” 的行， 可以做如下查询： `select * from table where city has any of ("New York", "Paris");` , 其中，用括号修饰的城市列表，相当于语法中的`IN` .

