# SQL 函数参考

您可以在SQL查询中使用函数。

## SQL 函数

使用函数，您可以转换、计算、组合或合并当前表中其他列的值。函数之间可以相互引用。 SQL 支持的函数与 SeaTable 支持的公式大致相同。

函数的基本语法如下：

```
FunctionName(parameters...)

```

参数可以是数字、字符串、常量、列名或者其他函数。被引用的列名称不能是别名。如果列名包含"-",您可以使用"\`"将列名括起来。

当前SQL查询提供下列函数：

* 操作符
* 数学函数
* 文本函数
* 日期函数
* 逻辑函数
* 统计函数

在这篇文档中，我们会提供所有函数的完整介绍，并提供相应的例子。如果您想查找特定的函数，可以通过Ctrl+F在当前页面进行查找。

## 函数及例子

您可以在SQL查询中使用下列常量：

| 操作符     | 描述                  | 输入      | 结果         |
| :------ | :------------------ | :------ | :--------- |
| e       | 返回自然常数 e=2.71828... | e+1     | 3.71828183 |
| pi      | 返回圆周率pi Pi.         | pi      | 3.14159265 |
| true()  | 返回逻辑值 'true'.       | true()  | true       |
| false() | 返回逻辑值 'false'.      | false() | false      |

### 操作符

操作符函数的参数类型必须是字符串或者数字。对于需要数字类型的参数，如果输入一个字符串，会自动尝试将字符串转换为数字；反之亦然。

| 操作符                                | 描述               | 输入                                                          | 结果                                |
| :--------------------------------- | :--------------- | :---------------------------------------------------------- | :-------------------------------- |
| add(num1,num2)                     | 计算两个值的和。         | add(1,2)                                                    | 3                                 |
| subtract(num1,num2)                | 计算两个值的差。         | subtract(5,4)                                               | 1                                 |
| multiply(num1,num2)                | 计算两个值的乘积。        | multiply(3,4)                                               | 12                                |
| divide(num1,num2)                  | 计算两个数相除。         | divide(3,2)                                                 | 1.5                               |
| mod(num1,num2)                     | 计算两个数的余数。        | mod(15,7)                                                   | 1                                 |
| power(num1,num2)                   | 返回某数的乘幂。         | power(3,2)                                                  | 9                                 |
| greater(num1,num2)                 | 判断一个数是否大于另一个数。   | greater(2,3)                                                | false                             |
| lessthan(num1,num2)                | 判断一个数是否小于另一个数。   | lessthan(2,3)                                               | true                              |
| greatereq(num1,num2)               | 判断一个数是否大于等于另一个数。 | greatereq(2,3)                                              | false                             |
| lessthaneq(num1,num2)              | 判断一个数是否小于等于另一个数。 | lessthaneq(2,3)                                             | false                             |
| equal(num1,num2)                   | 判断一个数是否等于另一个数。   | equal(\`Old price\`, \`New price\`)                         | false                             |
| unequal                            | 判断一个数是否不等于另一个数。  | unequal(\`Old price\`, \`New price\`)                       | true                              |
| concatenate(string1, string2, ...) | 将多个文本值连接为单个文本值。  | concatenate(\`Supplier\`, " has the product ", \`Product\`) | Microsoft has the product Windows |

### 数学函数

操作符函数的参数类型必须是数字。如果输入一个字符串，会自动尝试将字符串转换为数字。

| 操作符                           | 描述                                                                                                                                                                                      | 输入                 | 结果         |
| :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------- | :--------- |
| abs(number)                   | 返回一个数的绝对值。                                                                                                                                                                              | abs(-2)            | 2          |
| ceiling(number, significance) | 将数字向上舍入到最接近的整数或最接近的指定基数的倍数。(如果任何一个参数是非数值型，则 CEILING 返回空。  不论参数 number 的符号如何，数值都是沿绝对值增大的方向向上舍入。 如果 number 正好是 significance 的倍数，则不进行舍入。 如果 number 和 significance 都为负，则对值按远离 0 的方向进行向下舍入。) | ceiling(2.14)      | 3          |
|                               | 如果 number 为负，significance 为正，则对值按朝向 0 的方向进行向上舍入，                                                                                                                                        | ceiling(-2.14, 4)  | 0          |
| even(number)                  | 将正数向上舍入到最近的偶数，负数向下舍入到最近的偶数。                                                                                                                                                             | even(2.14)         | 4          |
| exp(number)                   | 返回 e 的 n 次方。                                                                                                                                                                            | expr(1)            | 2.71828... |
| floor(number, significance)   | 将数字向下舍入到最接近的整数或最接近的指定基数的倍数。(如果任一参数为非数值型，则 FLOOR 返回 空 。  如果 number 为正值且指定的基数为负，则 FLOOR 返回 空 。  如果 number 的符号为正，则数值向下舍入，并朝零调整。 如果 number 的符号为负，则数值沿绝对值减小的方向向下舍入。）                         | floor(2.86)        | 2          |
|                               | 如果 number 的符号为负，则数值沿绝对值减小的方向向下舍入。 如果 number 正好是 significance 的倍数，则不进行舍入。                                                                                                                | floor(-3.14, 5)    | \-5        |
| int(number)                   | 将数值向下取整为最接近的整数。                                                                                                                                                                         | int(-3.14)         | \-4        |
| lg(number)                    | 返回给定数值以 10 为底的对数。                                                                                                                                                                       | lg(100)            | 2          |
| log(number, base)             | 根据给定底数返回数字的对数。                                                                                                                                                                          | log(81, 3)         | 4          |
|                               | 如果底数没有指定，默认以10作为底数。                                                                                                                                                                     | log(1000)          | 3          |
| odd(number)                   | 将正(负)数向上(下)舍入到最接近的奇数。                                                                                                                                                                   | odd(-2.14)         | \-1        |
| round(number, digits)         | 按指定的位数对数值进行四舍五入。如果 num_digits 等于 0，则将数字四舍五入到最接近的整数。                                                                                                                                     | round(3.14)        | 3          |
|                               | 如果 num_digits 大于 0（零），则将数字四舍五入到指定的小数位                                                                                                                                                   | round(3.14, 1)     | 3.1        |
|                               | 如果 num_digits 小于 0，则在小数点左侧前几位进行四舍五入。                                                                                                                                                    | round(3.14, -3)    | 0          |
| rounddown(number, digits)     | 向下舍入数字。（如果 num_digits 大于 0（零），则将数字向下舍入到指定的小数位。 如果 num_digits 等于 0，则将数字向下舍入到最接近的整数。 如果 num_digits 小于 0，则在小数点左侧前几位进行向下舍入。）                                                                | rounddown(3.12, 1) | 3.1        |
| roundup(number, digits)       | 向上舍入数字。（如果 num_digits 大于 0（零），则将数字向上舍入到指定的小数位。 如果 num_digits 等于 0，则将数字向上舍入到最接近的整数。 如果 num_digits 小于 0，则在小数点左侧前几位进行向上舍入。）                                                                | roundup(-3.15)     | \-4        |
| sign(number)                  | 返回数字的正负号: 为正时，返回 1；为零时，返回 0；为负时，返回 -1。                                                                                                                                                  | sign(-2)           | \-1        |
| sqrt(number)                  | 返回某数的平方根。                                                                                                                                                                               | sqrt(81)           | 9          |

### 文本函数

| 操作符                                                    | 描述                                                                               | 输入                                                | 结果                   |
| :----------------------------------------------------- | :------------------------------------------------------------------------------- | :------------------------------------------------ | :------------------- |
| exact(string1, string2)                                | 返回两个数字符串是否相等。                                                                    | exact('SeaTable', 'Seatable')                     | false                |
| find(findString, sourceString, startPosition)          | 获取在一个字符串在另一个字符串中的索引。如果找不到，那么返回 0。(区分大小写)。                                        | find('Sea', 'seaTable', 1)                        | 0                    |
| left(string, count)                                    | Returns the specified number (count) of characters at the beginning of a string. | left('SeaTable', 3)                               | Sea                  |
| len(string)                                            | 从一个文本字符串的第一个字符开始返回指定个数的字符。                                                       | len('SeaTable')                                   | 8                    |
| lower(string)                                          | 将字符串转换为小写。                                                                       | lower('German)                                    | german               |
| mid(string, startPosition, count)                      | 从文本字符串中指定的起始位置起返回指定长度的字符。                                                        | mid('SeaTable is the best', 1, 8)                 | SeaTable             |
| replace(sourceString, startPosition, count, newString) | 将一个字符串中的部分字符用另一个字符串替换。                                                           | replace('SeaTable is the best.', 1, 8, 'Seafile') | Seafile is the best. |
| rept(string, number)                                   | 将字符串重复 nunber 次。                                                                 | rept('Sea ', 3)                                   | SeaSeaSea            |
| right(string, count)                                   | 从一个文本字符串的最后一个字符开始返回指定个数的字符。                                                      | right('SeaTable', 5)                              | Table                |
| search(findString, sourceString, startPosition)        | 返回一个指定字符或文本字符串在字符串中第一次出现的位置，从左到右查找(忽略大小写)。                                       | search('Sea', 'seaTable', 1)                      | 1                    |
| substitute(sourceString, oldString, newString, index)  | 将字符串中的部分字符串以新字符串替换。                                                              | substitute('SeaTableTable', 'Table', 'file', 1)   | SeafileTable         |
| T(value)                                               | 检测给定值是否为文本，如果是文本按原样返回，如果不是文本则返回空文本。                                              | T('123')                                          | 123                  |
| text(number, format)                                   | 根据指定的数值格式将数字转成文本。格式参数 format_text 可以为 number, percent, yuan, dollar, euro 中的一个。  | text(150, 'euro')                                 | €150                 |
| trim(string)                                           | 移除字符串两端的空格。                                                                      | trim(' SeaTable ')                                | SeaTable             |
| upper(string)                                          | 将字符串转换为大写。                                                                       | upper('German)                                    | GERMAN               |
| value(string)                                          | 将一个代表数值的文本字符串转换成数值。                                                              | value('123')                                      | 123                  |

### 日期函数

日期函数的输入参数必须是时间或者日期类型。输入常量时，以字符串表示，格式可以是 "2021-09-01 12:00:01" 或者 "2021-09-01"。当在 select 语句中返回日期公式结果时，如果函数的返回类型是时间或者日期，那么会被转换为[RFC3339 格式的字符串](https://www.rfc-editor.org/rfc/rfc3339.html)，比如 "2021-09-03T00:00:00+08:00"。需要注意的是，如果公式返回类型为时间或者日期，那么返回的结果不能作为参数传给数学函数、字符串函数。

| 操作符                                                      | 描述                                                                                          | 输入                                                   | 结果                  |
| :------------------------------------------------------- | :------------------------------------------------------------------------------------------ | :--------------------------------------------------- | :------------------ |
| date(year, month, day)                                   | 从输入的年、月和日返回国际格式 (ISO) 的日期。                                                                  | date(2021, 1, 3)                                     | 2021-01-03T00:00:00+08:00 |
| dateAdd(date, count, unit)                               | 增加时间。最后一个参数 unit 可以为 years, months, weeks, days, hours, minutes, seconds 中的一个。              | dateAdd('2020-02-03', 2, 'days')                     | 2020-02-05T00:00:00+08:00 |
| datedif(startDate, endDate, unit)                        | 计算两个日期之间相隔的秒数、天数、月数或年数。参数 unit 可以为 S, Y, M, D, YD, YM, MD. 中的一个。                            | dateDif('2018-01-01', '2020-01-01')                  | 2                   |
|                                                          | unit参数是可选的: S (秒数), D (天数), M (月数), Y (年数), YD (天数，忽略年份), YM (月份，忽略年份和天数), MD (天数，忽略年份和月份). | dateDif('2019-10-11', '2020-12-12', 'M')             | 14                  |
| day(date)                                                | 返回一个月中的第几天的数值，介于 1 到 31 之间                                                                  | day('2020-01-03)                                     | 3                   |
| eomonth(startDate, months)                               | 返回一个日期，表示指定日期之前或之后的几个月的最后一天。                                                                | eomonth('2020-01-01', 1)                             | 2020-02-29T00:00:00+08:00 |
|                                                          | 如果给定的数字（months）为负数，则表示之前的几个月的最后一天。                                                          | eomonth('2020-01-01', -1)                            | 2019-12-31T00:00:00+08:00 |
| hour(date)                                               | 返回小时数值，是一个 0 (12:00 A.M.) 到 23 (11:00 P.M.) 之间的整数。                                          | hour('2020-02-14 13:14:52)                           | 13                  |
|                                                          | 如果不包含小时，则返回0。                                                                               | hour('2020-02-14)                                    | 0                   |
| hours(startDate, endDate)                                | 返回两个日期之间的小时数。                                                                               | hours('2020-02-14 13:14', '2020-02-14 15:14')        | 2                   |
|                                                          | 如果日期中不包含小时，则认为是在该天的0时。                                                                      | hours('2020-02-14', '2020-02-14 15:14')              | 15                  |
| minute(date)                                             | 返回分钟数值，是一个 0 到 59 之间的整数。                                                                    | minute('2020-02-14 13:14:52                          | 14                  |
|                                                          | 如果日期中不包含分钟，则返回0。                                                                            | minute('2020-02-14)                                  | 0                   |
| month(date)                                              | 返回月份值，是一个 1 (一月)到 12 (十二月)之间的数字。                                                            | month('2020-02-14 13:14:52)                          | 2                   |
| months(startDate, endDate)                               | 返回两个日期之间的月数。                                                                                | months('2020-02-01 13:14', '2020-03-31 15:54')       | 1                   |
|                                                          | 如果日期不包含月份，则默认为1月。                                                                           | months('2020', '2021')                               | 12                  |
| networkdays(startDate, endDate, holiday1, holiday2, ...) | 返回两个日期之间的完整工作日数。                                                                            | networkdays('2020-01-01', '2020-01-07','2020-01-01') | 4                   |
| now()                                                    | 获取现在的时间。                                                                                    | now()                                                | 2020-09-07T12:59:00+08:00    |
| second(date)                                             | 返回秒数值，是一个 0 到 59 之间的整数。                                                                     | second('2020-02-14 13:14:52')                        | 52                  |
| today()                                                  | 获取今天的日期。                                                                                    | today()                                              | 2020-09-07T00:00:00+08:00 |
| weekday(date, weekStart)                                 | 返回代表一周中的第几天的数值，是一个 1 到 7 之间的整数。                                                             | weekday('2020-01-01', 'Monday')                      | 3                   |
| weeknum(date, return_type)                               | 返回特定日期的周编号，包含1月1日的星期是当年的第一周，并编号为第 1 周。                                                      | weeknum('2020-01-12', 11)                            | 2                   |
| year(date)                                               | 返回日期的年份值，一个 1900-9999 之间的数字。                                                                | year('2020-01-01')                                   | 2020                |
| startofweek(date, weekStart)                             | 返回日期所在周的第一天，weekStart 默认是 sunday，也可以设置为 monday。                                             | startofweek('2021-04-28')                            | 2021-4-25T00:00:00+08:00  |
| quarter(date)                                            | 返回日期所在季度，返回值为 1, 2, 3, 4。                                                                   | quarter('2021-01-01')                                | 1                   |
| isodate(date)                                            | 返回日期的 ISO 字符串表示，比如 "2021-05-11"。                                                            | isodate('2021-01-01 11:00:00')                       | 2021-01-01          |
| isomonth(date)                                           | 返回年月的 ISO 字符串表示，比如 "2020-05"。                                                               | isomonth('2021-01-01 11:00:00')                      | 2021-01             |

### 逻辑函数

| 操作符                                                               | 描述                                                  | 输入                                                                                      | 结果        |
| :---------------------------------------------------------------- | :-------------------------------------------------- | :-------------------------------------------------------------------------------------- | :-------- |
| and(logical1, logical2, ...)                                      | 检查是否所有参数均为 TRUE，如果所有参数值均为 TRUE，则返回 TRUE。            | and(1, '', 2)                                                                           | false     |
| if(logical, value1, value2)                                       | 判断是否满足某个条件，如果满足返回一个值，如果不满足则返回另一个值。                  | if(1>2, 3, 4)                                                                           | 4         |
| ifs(logical1, value1, logical2, value2, ...)                      | 检查是否满足一个或多个条件并返回与第一个 TRUE 条件对应的值                    | ifs( 1>2, 3, 5>4, 9)                                                                    | 9         |
| not(boolean)                                                      | 对参数的逻辑值求反: 参数为 TRUE 时返回 FALSE；参数为 FALSE 时返回 TRUE。   | not(and(1, '', 2))                                                                      | true      |
| or(logical1, logical2, ...)                                       | 如果任一参数值为 TRUE，即返回 TRUE；只有当所有参数值均为 FALSE 时才返回 FALSE。 | or(1,'',2)                                                                              | true      |
| switch(logical, matcher1, value1, matcher2, value2, ..., default) | 根据值列表求值表达式并返回与第一个匹配值对应的结果。如果没有匹配项，则返回可选默认值。         | switch(\`grades\`, 1, 'very good', 2, 'good', 3, 'satisfactory', 4, 'passed', 'failed') | very good |
| xor(logical1, logical2, ...)                                      | 返回所有参数的逻辑“异或”值。                                     | xor(1, 0, 2\<1)                                                                         | false     |

### 统计函数

| 操作符                                           | 描述                                                  | 输入                      | 结果  |
| :-------------------------------------------- | :-------------------------------------------------- | :---------------------- | :-- |
| average(number1, number2, ...)                | 返回一组数的平均值。                                          | average(1, 2, 3, 4, 5)  | 3   |
| counta(textORnumber1, textORnumber2, ...)     | Counts the number of non-e计算一组值中非空值的个数。非空值包括数字和字符串。 | counta(1, '', 2, '3')   | 3   |
| countall(textORnumber1, textORnumber2, ...)   | 计算一组值的个数 (包括空值)。                                    | countall(1, '', 2, '3') | 4   |
| countblank(textORnumber1, textORnumber2, ...) | countblank(textOrNumber1, \[textOrNumber2, ...])    | countall(1, '', 2, '3') | 1   |

