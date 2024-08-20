# SQL 支持

SeaTable 中数据查询支持 SQL 语句。使用 SQL 语句会检索完整的数据集，也就是包括归档和非归档的数据。

## 语法

目前只支持基本的 SELECT，INSERT，UPDATE，DELETE 语句。（INSERT，UPDATE，DELETE 语句于 2.7 版本起支持）

SELECT 语句的语法如下：

```SQL
SELECT [DISTINCT] fields FROM table_name [WhereClause] [GroupByClause] [HavingClause] [OrderByClause] [Limit Option]
```

从 4.3 版本起，支持基本的 JOIN 查询，例如：

```SQL
SELECT ... FROM table1, table2 WHERE table1.column1 = table2.column2 AND ...
```

JOIN 查询存在以下限制：

* 只支持 INNER JOIN 查询，不支持 LEFT JOIN，RIGHT JOIN，FULL JOIN 等。
* `FROM` 子句中的表不能重复。
* `FROM` 子句中的每个表必须至少关联一个 JOIN 条件。
* JOIN 条件需要放在 `WHERE` 子句里，并且用 `AND` 连接。
* JOIN 条件只能是两个列的相等比较，例如 `table1.column1 = table2.column2`。
* JOIN 条件中的列需要存在索引，除非这个子表未归档。

说明：

* where 语句中支持大部分的表达式（算数表达式，比较表达式等），关键字包括： `[NOT] LIKE`, `IN`, `BETWEEN ... AND ...`, `AND`, `OR`, `NOT`, `IS [NOT] TRUE`, `IS [NOT] NULL`. 其中：
    * 算术表达式只支持数字。
    * `LIKE` 语句只支持字符串。支持使用 `ILIKE` 关键字替代 `LIKE`，从而在匹配中不区分大小写。
    * `BETWEEN ... AND ...` 语句只支持数字与时间
    * 时间常量应该是 ISO 格式的字符串（如: "2020-09-08 00:11:23"）。从 2.8 版本开始，还支持符合 RFC 3339 标准的时间字符串，例如 "2020-12-31T23:59:60Z"。
* `GROUP BY` 语法比较严格。除了聚合函数的关键字（`COUNT`, `SUM`, `MAX`, `MIN`, `AVG`）以及公式（细节请查看本文档的扩展语法）之外，所选字段也必须同样也要出现在 group by 的语句中。
* `HAVING` 过滤经 group by 聚合后的行。只有 group by 语句中的字段或者聚合函数能被 having 语句引用，其它语法和 where 语句相同。
* "order by" 语句表示根据某字段排序，该字段必须出现在 select 表达式中。比如：`select a from table order by b`是无效语句；而 `select a from table order by a` 或者 `select abs(a), b from table order by abs(a)` 则可以运行。
* Limit 语句和 MySQL 格式一样，语法是 `LIMIT ... OFFSET ...`。
* 支持通过 AS 语法对返回的字段指定别名（alias）。例如 `select table.a as a from table`，则返回结果中的列名称为 "a"。有两点需要注意：
    * 一个返回字段的别名，可以在 group by, order by, having 语句中被引用。比如 `select t.registration as r, count(*) as c from t group by r having c > 100`。
    * 一个返回字段的别名，不能在 where 语句中被引用。比如 `select t.registration as r, count(*) from t group by r where r > "2020-01-01"` 会报告语法错误。

查询结果是以 JSON 的格式进行返回，每一行是一个 JSON 对象。默认情况下，对象的 key 是对应的列的 key，而不是列名。不过在 JOIN 查询里，对象的 key 对应 "id" 字段，而不是 "key" 字段。上述 "id", "key" 字段都存在于返回结果的 "metadata" 数组中。

INSERT，UPDATE，DELETE 语句的语法如下：

```SQL
INSERT INTO table_name [column_list] VALUES value_list [, ...]

UPDATE table_name SET column_name = value [, ...] [WhereClause]

DELETE FROM table_name [WhereClause]

```

* `column_list` 是一个由括号包围逗号分隔的列名列表，如果没有指定，则默认为所有可更新的列。
* `value_list` 是一个由括号包围逗号分隔的值列表，值必须和 `column_list` 中的列名一一对应。例如：`(1, "2", 3.0)` 。
* 多值列（如多选类型）需要使用括号包围值列表，例如 `(1, "2", 3.0, ("foo", "bar"))` 。
* 单选和多选类型的列需要使用选项名称，而不是选项 key。
* `WhereClause` 是一个可选的 where 语句，如果没有指定，则包含所有行。
* `INSERT` 语句仅支持已经归档过的 base 使用，数据会被直接插入大数据存储中。如果 base 未归档过，则会报错。如果需要往未归档过的 base 中插入数据，可以使用添加行的 API（比如 [Python API](../python/rows.md)）。
* `UPDATE` 和 `DELETE` 语句支持同时修改已归档和未归档的数据。

注意：以下列类型不支持插入和更新：

* 系统列（如 `_id`，`_ctime`）
* 图片，文件，公式，链接，链接公式，地理位置，自动序号，按钮

## 数据类型

以下表格列出了 SeaTable 表格中的数据与 SQL 语句字段中数据类型的对应情况

| SeaTable 数据类型 | SQL 字段类型 | 返回结果格式说明 | 用于 where/having | 用于 group by/order by |
| :---------------- | :---------| :------------- | :---------------- | :---------------------|
| 文本              | String     |                | 支持               | 支持                  |
| 长文本            | String     | 返回 Markdown 格式的原始字符串 | 支持                | 支持                  |
| 数字              | Float      |                | 支持               | 支持                  |
| 单选              | String     | 查询结果默认返回的是选项的 key ，如需返回选项的名称，则应把查询请求中的 `convert_key` 参数设置为 TRUE | 在 where 表达式中，常量需要使用选项的名称，如：`where single_select = "New York"` | 按照选项的定义顺序进行排序 |
| 多选              | 包含 string 的列表 | 查询结果默认返回的是选项的 key，如需返回选项的名称，则应把查询请求中的 `convert_key` 参数设置为 TRUE | 在 where 表达式中，需要使用选项的名称。具体的匹配规则参考下面关于列表类型的说明。 | 支持，参考下面关于列表类型的说明 |
| 勾选              | Bool       |                | 支持               | 支持                  |
| 日期              | Datetime   | 返回符合 RFC 3339 规范的字符串 | 查询时，常量使用 ISO 格式的时间字符串，如:  "2006-1-2"，"2006-1-2 15:04:05"。2.8 版本起，支持符合 RFC 3339 规范的字符串，例如 "2020-12-31T23:59:60Z" | 支持 |
| 地理位置          | 查询结果以 json 的格式进行返回。数据根据设置的格式不同返回结果有差异，如设置经纬度，返回经纬度的数字，设置省市等，返回省，市，其他细节信息等。| 不支持直接使用 where 语句查询，但是可以通过地理位置函数提取省市等细节信息进行过滤 | 不支持 | 不支持 |
| 图片              | 图片的 URL 的列表 | JSON 字符串数组，元素为 URL | 支持，参考下面关于列表类型的说明 | 支持，参考下面关于列表类型的说明 |
| 文件              | 查询结果将以 JSON 的格式进行返回，返回包含名称，类型，url等信息的列表 | 不支持 | 不支持 | 不支持 |
| 协作人            | 包含用户 ID 的列表 | 格式如 5758ecdce3e741ad81293a304b6d3388@auth.local, 如果用到用户名称，需要通过 SeaTable 的相关 API 进行转换 | 支持，参考下面关于列表类型的说明 | 支持，参考下面关于列表类型的说明 |
| 链接其他记录      | 包含链接行的列表 | 支持，参考下面关于列表类型的说明 | 支持，参考下面关于列表类型的说明 | 支持，参考下面关于列表类型的说明 |
| 公式              | 数据类型根据通过该公式计算得到的返回值类型而定 | 根据通过该公式计算得到的返回值类型而定，具体参考返回类型对应的 SQL 类型的说明 | 根据通过该公式计算得到的返回值类型而定，具体参考返回类型对应的 SQL 类型的说明 | 根据通过该公式计算得到的返回值类型而定，具体参考返回类型对应的 SQL 类型的说明 |
| 创建者            | 用户 ID, string |格式如 5758ecdce3e741ad81293a304b6d3388@auth.local, 如果用到用户名称，需要通过 SeaTable 的相关 API 进行转换 | 支持 | 支持 |
| 创建时间          | Datetime | 返回符合 RFC 3339 规范的字符串 | 查询时，常量使用 ISO 格式的时间字符串，如:  "2006-1-2"，"2006-1-2 15:04:05"。2.8 版本起，支持符合 RFC 3339 规范的字符串，例如 "2020-12-31T23:59:60Z" | 支持 |
| 修改者            | 用户 ID, string | 格式如 5758ecdce3e741ad81293a304b6d3388@auth.local, 如果用到用户名称，需要通过 SeaTable 的相关 API 进行转换 | 支持 | 支持 |
| 修改时间          | Datetime | 返回符合 RFC 3339 规范的字符串 | 查询时，常量使用 ISO 格式的时间字符串，如:  "2006-1-2"，"2006-1-2 15:04:05"。2.8 版本起，支持符合 RFC 3339 规范的字符串，例如 "2020-12-31T23:59:60Z" | 支持 |
| 自动序号          | String |          | 支持 | 支持 |
| URL               | String |          | 支持 | 支持 |
| 邮箱              | String |          | 支持 | 支持 |
| 时长                | Float | 数据换算成秒返回，如数据是3:43，换算成秒为3 * 3600 + 43 * 60 = 13380 | 支持 | 支持 |

### 列表类型的处理

SeaTable 中有两类列会产生列表数据类型：

* 本身就是列表类型的列：包括多选、图片、协作人、链接其他记录。
* 链接公式的返回结果：公式列中的公式为 `{link.column}` 以及 lookup 公式；链接公式列中的公式为 lookup, findmin, findmax。

当在 where 条件中使用一个类型为列表的列时，根据列表元素的 SQL 类型不同，规则如下：（如果没有列出则表示不支持）

| 元素类型      | 操作符                            | 规则                                                                        |
| :-------- | :----------------------------- | :------------------------------------------------------------------------ |
| string    | IN, 列表扩展语法（比如 has any of） | 按照相应的操作符规则处理                                                              |
| string    | LIKE, ILIKE                    | 始终取出第一个元素来比较；如果没有元素，按照 "" 来处理。         |
| string    | IS NULL                        | 没有数据或者空列表判断为 NULL                                                       |
| string    | =, !=                          | 如果只有一个元素，取出第一个元素来比较；如果有多于一个元素，只有在 != 的时候返回 true；如果没有元素，只有在 != 的时候返回 true。 |
| float     | IN, 列表扩展语法（比如 has any of） | 按照相应的操作符规则处理                                                              |
| float     | =, !=, \<, \<=, >, >=, between | 如果只有一个元素，取出第一个元素来比较；如果有多于一个元素，只有在 != 的时候返回 true；如果没有元素，只有在 != 的时候返回 true。 |
| float     | IS NULL                        | 没有数据或者空列表的时候判断为 NULL                                                    |
| float     | \+/-/\*// 等运算                  | 取出第一个元素参与运算                                                       |
| Datetime      | IN, 列表扩展语法（比如 has any of） | 按照相应的操作符规则处理                                            |
| Datetime      | =, !=, \<, \<=, >, >=, between | 如果只有一个元素，取出第一个元素来比较；如果有多于一个元素，只有在 != 的时候返回 true；如果没有元素，只有在 != 的时候返回 true。 |
| Datetime      | IS NULL                        | 没有数据或者空列表的时候判断为 NULL                                                    |
| bool      | IS TRUE                        | 始终取出第一个元素来比较；如果没有元素返回 false。 |
| 链接记录 |                                | 根据链接列设置的显示列的类型，结合上述每种类型的规则来处理                                          |

作为 select fields 返回的时候，只返回列表的前十个元素。

在 group by 和 order by 中使用时，会对每个列表内部的元素先进行从小到大的排序，然后在列表之间排序按照以下规则进行：

* 从第一个元素开始逐一比较大小，元素小的列表排在元素大的列表前面
* 如果之前遍历的元素都相等，则长度较小的列表排在长度大的列表前面
* 如果长度也相等，则两个列表相等

在公式中使用时，如果列表传入作为一个参数，而参数需要一个单值，则取出列表的第一个元素。如果列表的元素是一个链接记录，取出其显示列的值。

在聚合函数（min, max, sum, avg）中使用，如果列表只有一个元素，取出第一个元素来计算；其他情况，该行不参与计算。

### NULL 值

NULL 值不同于 0，它代表一个空值。以下的值会被看做空值：

* 表格中的空的单元格会被看做 NULL 值。
* 无法被转换为当前列类型的值，当作 NULL 值处理。
* 空字符串（""）会被看做 NULL 值。这与标准的 SQL 不一样。
* 列表类型的值根据“列表类型”一节中的规则被判断为 NULL。
* 公式列或函数如果返回了错误，会当作 NULL 值处理。

在 WHERE 条件中：

* 算术运算中存在 NULL 值，则结果为 NULL。
* `!=`，`NOT LIKE`，`NOT IN`，`NOT BETWEEN`，`HAS NONE OF`，`IS NOT TRUE` 和 `IS NULL` 遇到 NULL 值时结果是 TRUE。
* `AND`，`OR`，`NOT` 会把 NULL 值当作 FALSE 处理。
* 聚合函数（min，max，sum，avg）会忽略 NULL 值。

在公式中，NULL 值会被转换为 0 或者空字符串。

## 扩展语法

### SQL 查询中使用公式

 SeaTable 中的一些公式也可以用于 SQL 查询当中，以下有几点说明：

* 链接公式暂不支持，如 {link.age}，这种查询无效。
* 查询的列名不支持使用大括号(“{}”)来修饰，如：`select abs({column}) from talbe;` 属于无效查询，应该写成：`select abs(column) from table;`，此规则同 SQL 语法一致。
* 如果字段名称中包含空格或连接符“-”，可是使用左引号("\`\`")来进行修饰，如: select abs \`column-a\` from table。
* 不支持给子段起别名，如：`select abs(t.column) from table as t;` 为无效查询。
* 公式可以用在 group by 以及 order by 表达语句当中。

额外支持的公式函数：

* `STARTOFWEEK(date, weekStart)`：返回包含 “date” 的星期的第一天的日期，“weekstart” 可选 “sunday” 或者 “monday” 来作为一周的第一天
* `Quarter(date)`：返回第几个季度，包括1，2，3，4。
* `ISODate(date)`：返回 ISO 格式的日期，如: "2020-09-08"
* `ISOMonth(date)`：返回 ISO 格式的月份，如: "2020-07"

以上的公式可以用于 group by 分组，按星期，月，季度，日期等， 如：`select sum(sale) from SalesRecord group by ISODate(SalesTime)`，返回每天的总销量。

更多支持的公式函数请参考[SQL函数参考](function.md)

### 列表扩展语法

SeaTable 中部分的列类型数据格式为一个列表， SeaTable 从 UI 层面上提供了特殊的函数来过滤这些列， 包括`HAS ANY OF`, `HAS ALL OF`, `HAS NONE OF`, `IS EXACTLY`.  这些关键字同样也适用于 SQL 查询语法中。比如：名为 “city” 的列属于多选类型，我们想查询出所有包含 “New York” 和  “Paris” 的行，可以做如下查询：`select * from table where city has any of ("New York", "Paris");`，其中，用括号修饰的城市列表，相当于 `IN` 语法。

## 索引

为了提高查询效率，SeaTable 会为存储到大数据存储中的行自动创建索引。目前，文本、数字、单选、多选、协作人、日期、创建者、创建时间、修改者、修改时间列会创建索引。

当您在一个子表中新增或者删除一列时，对应的索引并不会立即自动创建或者删除。索引的创建和删除操作可以通过两种方式触发：

1. 在下次执行“归档”操作的时候，会自动为新增的列创建索引，并删除不存在的列的索引。
2. 用户可以通过“大数据管理” -> “索引管理” 界面来管理索引。
