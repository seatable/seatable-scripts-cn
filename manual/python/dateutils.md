# 时间操作函数DateUtils

我们在 python 的 datetime 模块的基础上提供一系列函数。这些函数和 SeaTable 中函数列提供的日期函数行为一致，方便用户对 SeaTable 中的日期进行处理。

时区处理: 所有的操作函数本地时区进行处理。如果输入带有时区信息的时间，那么先转换成本地时区时间然后处理。

#### 函数引入

```python
from seatable_api import dateutils
```

#### date

返回 ISO 格式化的日期字符串

```python
dateutils.date(2020, 5, 16) # 2020-05-16
```

#### now

返回 ISO 格式化的当前日期和时间字符串，精确到秒

```python
dateutils.now() # 2022-02-07 09:44:00
```

#### dateadd

对时间进行加法运算，通过传递不同的单位参数可以加年，月，周，日，小时，分钟，秒，默认使用‘日’作为单位

```python
time_str = "2020-6-15"
time_str_s = "2020-6-15 15:23:21"

dateutils.dateadd(time_str, -2, 'years') # 2018-06-15
dateutils.dateadd(time_str, 3, 'months') # 2020-09-15
dateutils.dateadd(time_str_s, 44, 'minutes') # 2020-06-15 16:07:21
dateutils.dateadd(time_str_s, 1000, 'days') # 2023-03-12 15:23:21
dateutils.dateadd(time_str_s, 3, 'weeks') # 2020-07-06 15:23:21
dateutils.dateadd(time_str_s, -3, 'hours') # 2020-06-15 12:23:21
dateutils.dateadd(time_str_s, 3, 'seconds') # 2020-06-15 15:23:24
```

#### datediff

计算两个日期之间相隔的秒数，天数， 月数，年数， 参数可以为 S, Y, M, D, YM, MD

其中

* YM, 开始时间与结束时间之间月份之差, 忽略日期中的天和年份
* MD, 开始时间与结束时间之间天数之差, 忽略日期中的月份和年份
* YD,  开始时间与结束时间的日期部分之差, 忽略日期中的年份。

```python
time_start = "2019-6-1"
time_end = "2020-5-15"
dateutils.datediff(start=time_start, end=time_end, unit='S') # seconds 30153600
dateutils.datediff(start=time_start, end=time_end, unit='Y') # years 0
dateutils.datediff(start=time_start, end=time_end, unit='D') # days 349
dateutils.datediff(start=time_start, end=time_end, unit='H') # hours 8376
dateutils.datediff(start=time_start, end=time_end, unit='M') # months 11
dateutils.datediff(start=time_start, end=time_end, unit='YM') #  11
dateutils.datediff(start=time_start, end=time_end, unit='MD') #  14
dateutils.datediff("2019-2-28","2020-2-1", unit='YD') # -27
```

#### eomonth

返回某个日期的前 n 个月或后 n 个月的最后一天， 参数为 months 代表 n

```python
date = "2022-7-4"
dateutils.eomonth(date, months=0) # 2022-07-31
dateutils.eomonth(date, months=2) # 2022-09-30
dateutils.eomonth(date, months=-5) # 2022-02-28
```

#### year

返回某个日期的年

```python
dateutils.year("2019-1-1") # 2019
```

#### month

返回某个日期的月

```python
dateutils.month("2019-5-4") # 5
```

#### months

返回两个日期相差的月数

```python
dateutils.months("2019-5-1","2020-5-4") # 12
```

#### day

返某个日期的天

```python
dateutils.day('2020-6-15 15:23:21') # 15
```

#### days

返回两个日期相差的天数

```python
dateutils.days('2019-6-1', '2020-5-15') # 349
```

#### hour

返回时间的小时数

```pyhton
dateutils.hour("2020-1-1 12:20:30") # 12
```

#### hours

返回两个日期相差的小时数

```python
dateutils.hours("2019-6-3 20:1:12", "2020-5-3 13:13:13") # 8033
```

#### minute

返回时间的分钟数

```python
dateutils.minute("2020-5-3 13:13:13") # 13
```

#### second

返回时间的秒数

```python
dateutils.second("2020-5-3 13:13:33") # 33
```

#### weekday

返回某个日期是星期几, 记周一为0， 周日为6

```python
dateutils.weekday("2019-6-3") # 0
```

#### isoweekday

基于iso标准，返回某个日期是星期几，记周一为1， 周日为7

```python
dateutils.isoweekday("2019-6-3") # 1
```

#### weeknum

返回某个日期是当年的第几周，含1月1日为第一周

```python
dateutils.weeknum('2012-1-2') # 2
```

#### isoweeknum

返回某个日期当年的 ISO 周计数， 即当年第一个周四开始记为第一周

```python
dateutils.isoweeknum('2012-1-2') # 1
```

#### isomonth

返回某个日期字符串的 ISO 格式的月份

~~~python
dateutils.isomonth("2012-1-2") # 2012-01
~~~

#### quarter_from_yq

返回一个季度对象，参数包含年份，季度。

```python
q = dateutils.quarter_from_yq(2022, 3) # <DateQuarter-2022,3Q>
```

#### quarter_from_ym

返回一个季度对象， 参数包含年份， 月份

```python
q = dateutils.quarter_from_ym(2022, 3) # <DateQuarter-2022,3Q>
```

#### to_quarter

返回某个日期字符串对应的季度(DateQuarter对象)

```python
time_str = "2022-07-17"
q = dateutils.to_quarter(time_str) # DateQuarter obj: <DateQuarter-2022,3Q>
```

#### quarters_within

返回开始日期，结束日期之间的季度， 返回一个生成器, 里面会产生DateQuarter 对象，包含参数 include_last 是否包含最后一个季度， 默认为 False

```python
qs = dateutils.quarters_within("2021-03-28", "2022-07-17", include_last=True) # 生成器
list(qs) # [<DateQuarter-2021,1Q>, <DateQuarter-2021,2Q>,...., <DateQuarter-2022,3Q>]
```

#### 季度操作

季度对象包含年，月等属性， 并且可以进行运算

```python
q = dateutils.quarter_from_yq(2022, 3)
# 获取年份， 季度, 开始结束日期等
q.year # 2022
q.quarter # 3

q.start_date # 2022-07-01
q.end_date # 2022-09-30

# 日期遍历
q.days()  # 生成器对象， 里面包含该季度所有日期
list(q.days()) # [datetime.date(2022, 7, 1), datetime.date(2022, 7, 2),....., datetime.date(2022, 9, 30)]

# 季度运算
q + 10 # <DateQuarter-2025,1Q> 2025年第一季度
q1 = dateutils.quater_from_yq(2021, 1) # <DateQuarter-2021,1Q>
q - q1 # 6
q < q1 # False
"2022-6-28" in q # False
"2022-8-28" in q # True
```

#### 时间处理举例

通过dateutils获取的日期信息，可以当作参数再次传递到dateutils的处理函数中去

```python
dt_now = dateutils.now()  # 2022-02-07 09:49:14
# 1. 获取10天后的时间
dt_10_days = dateutils.dateadd(dt_now, 10) # 2022-02-17 09:49:14
# 2. 获取10天后的月份
dt_month_10_days = dateutils.month(dt_10_days) # 2
# 3. 获取时间差，天数差
dt_10_days_before = dateutils.dateadd(dt_now, -10)
date_df = dateutils.datediff(dt_10_days_before, dt_10_days, unit="D") # 20

# 4. 处理有时区的时间字符串
time_str = "2021-07-17T08:15:41.106+00:00"
time_day = dateutils.day(time_str) # 17
time_month = dateutils.month(time_str) # 7
time_year = dateutils.year(time_str) # 2021
time_hour = dateutils.hour(time_str) # 16，因为北京时间比 UTC 时间多 8 小时
time_date = dateuitls.date(time_year, time_month, time_day) # 2021-07-17
```

注意，SQL 查询接口

* 对日期列类型返回的是 ISO 格式的服务器所在时区的时间字符串， 比如 `2021-07-17T00:00:00+08:00`
* 对创建时间列和最后修改时间列返回的是 ISO 格式的 UTC 时区的时间字符串。比如 `2021-07-17T08:15:41+00:00`

两种类型的时间都可以通过 Python 标准库中的 datetime 模块来处理。
