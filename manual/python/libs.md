# 云端环境下支持的库列表

在云端环境下，Python 脚本实际上是在一个 Docker 容器环境下运行。容器环境默认安装了一些 Python 库，这些库可以在脚本中导入。如果你需要用到其他的库，需要和我们联系，或者你的脚本只能在你的本地运行。

## Python 3 标准库

云端环境现在使用的是 Python 3.7, 支持导入 Python 标准库中的模块。

## 第三方库

如下模块可供使用

* SeaTable API 库, [seatable-api](https://pypi.org/project/seatable-api/)
* 日期/时间运算的工具库, [dateutils](https://pypi.org/project/dateutils/)
* http 请求库, [requests](https://pypi.org/project/requests/)
* OpenSSL 库, [pyOpenSSL](https://pypi.org/project/pyOpenSSL/)
* Pillow 库, [Pillow](https://pypi.org/project/Pillow/)
* Barcode 库, [python-barcode](https://pypi.org/project/python-barcode/)
* Pandas 库, [pandas](https://pypi.org/project/pandas/)
* Numpy 库, [numpy](https://pypi.org/project/numpy/)
