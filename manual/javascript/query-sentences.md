# Query-Sentence

通过 base.filter 的调用结合写入类 sql 的语句的方式可以灵活的对表格中数据进行查询， 其中不同的数据类型支持的查询方式，以及查询语句书写规范有些许差异，以下进行详细说明

## 操作符说明

* **大小比较:**  >， >=， =， \<， \<=
* **相异比较:**  =， \<>
* **数学运算:**  +, -, \*, /, ^, %

## 汇总

以 `queryset = base.filter("Table1", "age>18")` 中的语句为例：

* age: 列名，以下用 column_name 代替
* \> : 操作符
* 18: 查询参数

| 数据结构 | 列类型                   | 大小比较参数规范                                                                                                                      | 相异比较参数规范                   | 数学运算 |
| ---- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------- | :--- |
| 字符串  | 文本, 长文本, URL, 邮箱,  单选 | 不支持                                                                                                                           | 字符串, 空值 ""                 | 不支持  |
| 列表   | 多选                    | 不支持                                                                                                                           | 字符串                        | 不支持  |
| 数字   | 数字                    | 接受整数，小数                                                                                                                       | 接受整数，小数，空值“”               | 支持   |
| 日期   | 日期,  创建时间, 修改时间       | 接受日期格式的参数，规则如下：年-月-日 如 "2020-1-30", 年-月-日 时:分 如"2020-1-30 5:28", 年-月-日 时:分:秒 如 "2020-1-30 5:28:7" | 同大小比较参数规范相同，此外接受空值""       | 不支持  |
| 布尔   | 勾选                    | 不支持                                                                                                                           | 接受 True，False (不区分大小写)， 空值 | 不支持  |

## 举例说明

### 字符串数据结构列

* 包含**文本**，**长文本**， **URL**， **邮箱**，**单选**等列类型

```javascript
# 1. 相异比较
base.filter('Table1', 'view_name', "column_name=hello world")
base.filter('Table1', 'view_name', "column_name!=''")

```

### 列表数据结构列

* 包含**多选**等列类型

```javascript
// 相异比较
base.filter('Table1', 'view_name', "column_name=北京 and column_name=上海") # 同时包含“北京”和“上海”的行， and 可以替换成 or

```

### 数字数据结构列

* 数字类型数据的比较

```javascript
// 1. 大小比较
base.filter('Table1', 'view_name', "column_name>18")
base.filter('Table1', 'view_name', "column_name>-10 and column_name<=0")

// 2. 相异比较
base.filter('Table1', 'view_name', "column_name<>20")
base.filter('Table1', 'view_name', "column_name=0")
base.filter('Table1', 'view_name', "column_name=''")

```

* 数学运算

```javascript
base.filter('Table1', 'view_name', "column_name+3>18")
base.filter('Table1', 'view_name', "column_name*2=18")
base.filter('Table1', 'view_name', "column_name-2=18")
base.filter('Table1', 'view_name', "column_name/2=18")
base.filter('Table1', 'view_name', "column_name^2=18")
base.filter('Table1', 'view_name', "column_name%2=1")
```

### 日期数据结构列

* 包括**日期**，**创建时间**，**修改时间**等, 

```javascript
# 1. 大小比较
base.filter('Table1', 'view_name', "column_name>'2020-1-30'")
base.filter('Table1', "column_name>='2019-1-1 5:30' and column_name<='2019-5-1 6:00'")

# 2. 相异比较
base.filter('Table1', 'view_name', "column_name='2020-1-1 10:59:59'")
base.filter('Table1', 'view_name', "column_name!=''")

```

**注意: 日期比较需要把查询的日期加上引号**

### 布尔数据结构列

* **勾选**类型

```javascript
// 相异比较
base.filter('Table1', 'view_name', 'column_name=False') # 同 base.filter('Table1', 'view_name', "column_name=''")
base.filter('Table1', 'view_name', "column_name=True")

```