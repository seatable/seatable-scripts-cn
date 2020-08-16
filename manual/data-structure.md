# SeaTable 中对象的数据结构

## Row, Column, Table

### Row (行)

Row 是一个对象, 使用 `row['colum_name']` 可以访问特定列的内容. 有一些特殊的字段如下:

* `_id` : The id of the row
* `_creator` : The creator for this row
* `_ctime`: The create time for this row
* `_last_modifier` : The last modifier for this row
* `_mtime`: The last modified time for this row

不同的列类型的单元格的值有不同的数据类型，如下:

* `simple-text` : string
* `number` : number
* `single-select` : option name, string
* `date` : string, in format `2020-01-01` or `2020-01-01 10:00` 
* `check` : boolean
* `long-text` : Markdown string
* `image` : array, each element of the array is the URL of image
* `multi-select` : array, each element of the array is an option name
* `collaborator` : array, each element of the array is a collaborator's ID
* `link` : array, each element of the array is a link name
* `file` : array, each element of the array is a file object  `[{name: string, url: string, size: number, type: 'file'}]`

### Column (列)

一个 column 对象有以下的字段:

* `type` : The type of the column(long-text, single-select, number, file and so on), string
* `name` : The name of the table, string

### Table (子表)

一个 table 对象有以下的字段:

* `name` : The name of the table, string
