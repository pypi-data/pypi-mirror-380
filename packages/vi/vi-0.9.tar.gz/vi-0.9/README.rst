vi for labkit
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

in the cluster front server: `labkit front`

in the cluster node : `labkit worker`

and all above can be configured at the first time, and then you can only use
`labkit push` to submit your task. The wonderful journey is now started!

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
```
labkit push
```
to push a task.

labkit will run the task in the cluster automatically in parallel, and finally get the answer.

task.yml grammer
----------------

the extension of yaml config file is `.yml` and the default config file name is task.yml
if you run `labkit push` without any other arguments. `task.yml` in current folder will be push.

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

