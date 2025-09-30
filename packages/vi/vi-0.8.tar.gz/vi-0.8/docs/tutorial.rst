========
Tutorial
========

labkit
====================

labkit for the calculation and analysis of bio-physical design platform.
User-submitted tasks automatically in parallel.

labkit also offers a number of comprehensive practical Python library
, including

- general (please refer to the general lib ), the framework and public utility library
- compute
- ensemble

Quick start
===============
install
-------
simplely install labkit by

    sh install.sh

This will install labkit and it's frontend.

Preparation
------------
you need a linux cluster to run labkit

in the cluster front you need beanstalkd and mongodb running

in the cluster front server:
    `labkit front`

in the cluster node :
    `labkit worker`

and all above can be configured at the first time, and then you can only use
    `labkit push`

to submit your task. The wonderful journey is now started!

Concept
-------
labkit use yaml config file to describe algorithm, and when your config file is written, then simplely
push it to the server, the cluster will do all other things for you and return the answer.

when develop labkit, you can also easily add new modules and functions, and call them in the yaml config file.
all your new module can also be deal with correctly and automatically. also all labkit's origin module are running by this way.
you can easily contribute labkit so it can grow up and become more useful.


workflow
----------------
compose a task.yml file, and the module_settings, then use
    `labkit push`

to push a task.

labkit will run the task in the cluster automatically in parallel, and finally get the answer.

task.yml grammer
----------------

the extension of yaml config file is `.yml` and the default config file name is task.yml
if you run `labkit push` without any other arguments. `task.yml` in current folder will be push.

::

    list:

        - item1
        - item2

    map:

        key: value

    rule:
        - a list :        // undefined key without single value will be ignored
            - a list item is a single task and will be evaluated sequentially.
            - second item
          dict: function arguments, or assign a variable
          repeat: 100
          until: condition

Learning more about labkit
==========================

labkit is simple and easy use! the advanced usage is also simple and powerful!
It's just what you needed! The next step on your labkit journey is the `full user guide <guide/index.html>`_, where you
can learn indepth about how to use labkit and develop your own algorithm.


.. tutorial: 本地链接和readthedocs链接. 全面的教程
.. doc: 本地链接和readthedocs链接. 开发者教程
.. api: 本地链接和readthedocs链接. 参考api
.. labkit frontend: labkit website


labkit quick reference
================

worker : the process running in node

front : the process running in front to deal with the task

push : push a task.yml to the work queue

context : the variables which are persistent for all function to use during a task. It also record the position and state of current task for restore progress.


message are delivered by beanstalk

args will refresh context

message are in json

put({context:context, module_name:module_name})

example:

task:
  module_name: the module_name

  args:
    // function's arguments
    arg1:
    arg2:

  context:
    //include the state of current task, for restoring progress when come back.
    running_file: path to file
    running_job: path to job
    state: done/running


when every line done, it will change context, and context will refresh args.

context will be recorded persistently.

run function should return True or other value which is True.

push task.yml-> deal_with_line(push compute) -> compute worker

compute, conformer, and such module contains function applied to single conformer. which will be maped to the whole ensemble.

and some other module could contain filter and reduce function. all function will be dealed with properly.

ensemble function : delivery task for ensemble item, and calculate the statistics of the ensemble.

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
