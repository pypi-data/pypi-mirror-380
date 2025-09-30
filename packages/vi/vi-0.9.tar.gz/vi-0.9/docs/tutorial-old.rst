========
Tutorial
========


Getting started
===============

simply use pip to install it like so::

    $ pip install labkit
    $ pip install labkitfrontend

This will install labkit and it's frontend. The wonderful journey is now started!

Submit your first task
======================
After your installation, run the command in your terminal to start the labkit
service and it's frontend::
    $ labkit
    $ labkitfrontend

open your browser and enter::
    http://localhost:7777

to see the dashboard of labkit.

then submit a task to run.


See the result
--------------
the result is in the result section when the computing is done. Enjoy it!


Learning more about labkit
--------------------------

labkit is so simple and easy use! the advanced usage is als simple and powerful!
It's just what you needed! The next step on your labkit journey is the `full user guide <guide/index.html>`_, where you
can learn indepth about how to use labkit and develop your own algorithm.



# labit

labkit是为生物物理设计的计算和分析平台. 用户所提交的任务会自动并行.

labkit还提供大量全面的实用的python库.



## 启动

节点上: `labkit worker`
前端: `labkit front`
前端还需要启动: `beanstalkd, mongodb`
所有这些一开始配置好就行了, 使用时候只需要`labkit push`


## labkit workflow

编写task.yml, 配置默认的module_settings, 然后使用
```
labkit push
```
推入任务

labkit会自动将任务在集群上并行运算, 得到最终结果.

## task.yml 语法



rule:
  - list:
      - 列表就是任务, 每一个列表会自动执行
    dict: 函数调用, 或者赋值.
    labkit: labkit的自身的配置文件用ini格式, 全局统一, 请不要操心.




## labkit 快速参考

worker 节点上的工作进程

front 前端上的处理队列

push 添加任务

context 持久化的上下文, 记录当前的参数, 以及运行到的位置和状态.

beanstalk传递的信息:

用参数更新context, 传递json

put({context:context, module_name:module_name})

例子:

task:
  name: the module_name

  args:
    各种变量, 参数. 平铺
    arg1:
    arg2:


  context:
    包括记录当前运行状态的量, 用于恢复的时候处理.
    running_file: path to file
    running_job: path to job
    state: done/running


每运行完, 就会改变context, context会刷新args
context会保存下来, 可以恢复进度

run成功需要返回True或者其他真值

push task.yml-> deal_with_line(push compute) -> compute worker

单体的函数, compute, conformer, 执行该执行的功能
ensemble的函数, 针对ensemble进行分发, 针对ensemble进行统计

Commands:
  backup    backup all data to backup folder
  restore   restore all data from backup folder

  startdb   start mongodb and redis-server
  rest      start the rest api server
  start     ensure all service are running, start rest and server

  front     start the server to deal with task
  worker    start a worker to do the compute

  push      push a task to the tasks queue

  runner    run a task locally
