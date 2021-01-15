# Query-Sentence

通过 base.filter 的调用结合写入类 sql 的语句的方式可以灵活的对表格中数据进行查询， 其中不同的数据类型支持的查询方式，以及查询语句书写规范有些许差异，以下进行详细说明

## 操作符说明

* **大小比较:**  >， >， =， <， <=

* **相异比较:**  =， !=， <>(同!=)

* **模糊比较:**  like

## 汇总

以 `queryset = base.filter("Table1", "age>18")` 中的语句为例：

* age: 列名，以下用 column_name 代替
* \> : 操作符
* 18: 查询参数

| 数据结构 | 列类型                                        | 大小比较参数规范                                             | 相异比较参数规范                       | 模糊比较参数规范                                             |
| -------- | --------------------------------------------- | ------------------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------ |
| 字符串   | 文本<br />长文本<br />URL<br />邮箱<br />单选 | 不支持                                                       | 字符串                                 | 需要有“%”占位符，规则如下：<br /> %a: 匹配以“a”结尾的字符；<br />a%: 匹配以“a”开头的字符；<br />%a%: 匹配包含“a”的字符；<br />a%b: 匹配以“a”开头“b”结尾的字符 |
| 列表     | 多选                                          | 不支持                                                       | 字符串                                 | 不支持                                                       |
| 数字     | 数字                                          | 接受整数，小数                                               | 接受整数，小数，空值“”                 | 不支持                                                       |
| 日期     | 日期<br />创建时间<br />修改时间              | 接受日期格式的参数，规则如下：<br />年-月-日 --如 "2020-1-30"<br />年-月-日 时  如 "2020-1-30 5"<br />年-月-日 时:分 如"2020-1-30 5:28"<br />年-月-日 时:分:秒 如 "2020-1-30 5:28:7" | 同大小比较参数规范相同，此外接受空值"" | 不支持                                                       |
| 布尔     | 勾选                                          | 不支持                                                       | 接受 True，False (不区分大小写)， 空值 | 不支持                                                       |

## 举例说明

### 字符串数据结构列

* 包含**文本**，**长文本**， **URL**， **邮箱**，**单选**等列类型

```python
# 1. 相异比较
base.filter('Table1', "column_name=hello world")
base.filter('Table1', "column_name!=''")

# 2. 模糊比较
base.filter('Table1', "column_name like 百度%") # 找到以“百度”开头的文本的行
base.filter('Table1', "column_name like %建议%") # 找到包含“建议”两个字的文本的行
```

### 列表数据结构列

* 包含**多选**等列类型

~~~python
# 相异比较
base.filter('Table1', "column_name=北京 and column_name=上海") # 同时包含“北京”和“上海”的行， and 可以替换成 or
~~~

### 数字数据结构列

* **数字**类型

~~~python
# 1. 大小比较
base.filter('Table1', "column_name>18")
base.filter('Table1', "column_name>-10 and column_name<=0")

# 2. 相异比较
base.filter('Table1',"column_name<>20")
base.filter('Table1', "column_name=0")
base.filter('Table1',"column_name=''")
~~~

### 日期数据结构列

* 包括**日期**，**创建时间**，**修改时间**等, 

~~~python
# 1. 大小比较
base.filter('Table1', "column_name>'2020-1-30'")
base.filter('Table1', "column_name>='2019-1-1 5:30' and column_name<='2019-5-1 6'")

# 2. 相异比较
base.filter('Table1', "column_name='2020-1-1 10:59:59'")
base.filter('Table1', "column_name!=''")
~~~

**注意: 日期比较需要把查询的日期加上引号**

### 布尔数据结构列

* **勾选**类型

~~~python
# 相异比较
base.filter('Table1','column_name=False') # 同 base.filter('Table1', "column_name=''")
base.filter('Table1', "column_name=True")
~~~





