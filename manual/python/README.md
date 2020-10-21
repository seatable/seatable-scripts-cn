# SeaTable Python 脚本编程

Javascript 脚本来当前的浏览器中直接运行，适合于对数据进行简单的处理。Python 脚本在服务器端运行，而且可以设置自动周期性运行，适合于更复杂的数据处理场景。


## 编程参考

SeaTable 一般对象的数据结构:

* [数据结构](../data-structure.md)

SeaTable API 库介绍:

* [Base](base.md)
* [Context](context.md)

## 如何让脚本同时支持本地云端中运行

* Base授权登录

    Base初始化时，需要两个参数，在云端运行时从环境变量中获取，或者从context对象中获取(其实背后都是从环境变量中获取的)，所以如果脚本需要同时支持本地与云端，则本地运行时，在环境变量中设置好两个参数

* 表格/行 信息

    云端下context对象可以获取到当前表格/行信息，`context.dtable_web_url`, `context.api_token`，本地是不支持这两个属性的，所以要同时支持本地与云端，尽量避免context下的这两个属性

* 文件读写

    涉及到本地文件读写的脚本，不能够很好同时支持本地与云端。我们的初衷本也是使用脚本操作SeaTable，所以涉及到文件读写的操作，我们更加鼓励这种操作是针对SeaTable中的文件进行的，使用`base.get_file_download_link`, `base.get_upload_link`等接口
