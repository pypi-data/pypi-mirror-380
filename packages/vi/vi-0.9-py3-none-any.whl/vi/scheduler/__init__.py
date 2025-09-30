#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


# from  server import *


# sheduler模块, 就只处理队列的推送和抓取任务执行问题. yaml解析和算法处理都在interpreter模块. push和worker的调用, 也就是对外接口, 在cmd模块和api模块. 这里只处理逻辑.
# push和worker协同处理beanstalk队列, 队列中传递函数调用的dumps.
# 因为是通用的函数调用. sheduler模块处理的是通用的任务推送和执行的问题.
#
