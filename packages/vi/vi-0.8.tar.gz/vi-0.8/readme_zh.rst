labkit
====================

labkit是为生物物理设计的计算和分析平台. 用户所提交的任务会自动并行.

labkit还提供大量全面的实用的python库.包括

- general库(参看general库的介绍), 框架和公用实用库
- compute,
- ensemble

install
=========
sh install.sh

quick start
===========

预备
----
labkit 运行在linux集群上

前端需要启动: `beanstalkd, mongodb`
前端: `labkit front`
节点上: `labkit worker`

所有这些一开始配置好就行了, 使用时候只需要`labkit push`

概念
----
labkit使用配置文件描述算法, 当你写好描述算法和参数的配置文件的时候, 你已经完成了所有的编程工作, 你只需用`labkit push`
把它推送到集群, labkit会自动帮你处理所有的事情并且给你要计算的问题的结果.

当开发labkit的时候, 你可以非常简单的添加新的模块, 所有的模块可以被自动的处理成为并行的. labkit自身原有的模块也是如此.
你可以非常简单的贡献labkit, 使得它变得越来越好用.

流程
--------

编写task.yml, 配置默认的module_settings, 然后使用
```
labkit push
```
推入任务

labkit会自动将任务在集群上并行运算, 得到最终结果.

task.yml 语法
--------------
labkit使用yaml格式的配置文件, 扩展名是`.yml`. 默认的配置文件名是`task.yml`

如果不加参数运行`labkit push`, 当前目录下的`task.yml`将会被推送到服务器.

rule:
  - list:
      - 列表就是任务, 每一个列表会自动执行
    dict: 函数调用, 或者赋值.
    labkit: labkit的自身的配置文件用ini格式, 全局统一, 请不要操心.

进一步深入
=========
如果您想要学习labkit, 或者开发labkit, 请参阅以下内容

tutorial: 本地链接和readthedocs链接. 全面的教程
doc: 本地链接和readthedocs链接. 开发者教程
api: 本地链接和readthedocs链接. 参考api
labkit frontend: labkit website

