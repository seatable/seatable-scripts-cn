# Row, Column, Table, View

## Row (行)

Row 是一个对象, 使用 `row['colum_name']` 可以访问特定列的内容. 有一些特殊的字段如下:

* `_id` : The id of the row
* `_creator` : The creator for this row
* `_ctime`: The create time for this row, 记录的是 UTC 时区的 ISO 格式的时间 (比如 2022-04-14T09:51:54.159+00:00)。
* `_last_modifier` : The last modifier for this row
* `_mtime`: The last modified time for this row, 记录的是 UTC 时区的 ISO 格式的时间 (比如 2022-04-14T09:51:54.159+00:00)。

## Column (列)

一个 column 对象有以下的字段:

* `key` : The key of the column, string
* `type` : The type of the column(long-text, single-select, number, file and so on), string
* `name` : The name of the column, string

不同的列类型的单元格的值有不同的数据类型，如下:

基本列类型:

* `text` : string
* `number` : number
* `checkbox` : boolean
* `date` : string, in format `2020-01-01` or `2020-01-01 10:00` 
* `single-select` : option name, string
* `long-text` : markdown string
* `image` : array, each element of the array is the URL of image
* `file` : array, each element of the array is a file object  `[{name: string, url: string, size: number, type: 'file'}]`
* `multi-select` : array, each element of the array is an option name
* `collaborator` : array, each element of the array is a collaborator's system ID
* `URL` : string
* `email` :  string
* `duration` : string, in format `h:mm(1:30)` or `h:mm:ss(0:20:30)` 
* `rating`: number, indicates a rating

高级列类型:

* `formula` : string
* `geolocation` : object, in format `{province: xxx, city: xxx, district: xxx, detail: xxx}`
* `link` : array, each element of the array is a link name
* `auto-number` : number, auto increase

## Table (子表)

一个 table 对象有以下的字段:

* `_id`: The id of the table 

* `name` : The name of the table, string

## View (视图)

一个视图对象有以下字段:

* `name`: The name of the view, string
