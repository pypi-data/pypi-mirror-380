#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

# from general import gs
# import labkit.init_gs

# import sys
# sys.argv[1:]=[]
#

#
# @register
# def push_to(queue_names='tasks',yml_file='task.yml'):
#     '''
#     push a task to a specific queue
#
#     :param queue_names:
#     :return:
#     '''
#     # push
#     import sys
#     from labkit.scheduler.push_task_file import push_file
#     # queue_names=queue_names.split()
#     sys.exit(push_file(queue_names))

'''
the command line interface for labkit

'''

import sys

from general.cli import (
    kwoargs,autokwoargs,wrapper_decorator,
    register_maker,run,subprocess_shell,subprocess_run
)
import os

register,_functions=register_maker()

# redis_dir='/usr/local/var/db/redis'

beanstalk_dir='/usr/local/var/binlog'

from general.reflection import get_script_location

labkit_dir=get_script_location(__file__)
import os
for i in range(4):
    labkit_dir=os.path.dirname(labkit_dir)

# print labkit_dir

# @register
def service(command):
    '''
    control labkit services

    :param command:
    :return:
    '''
    if command == 'start':
        print "labkit front and worker service started"
    if command == 'stop':
        print "labkit front and worker service stoped"


@register
def new(project_name):
    '''
    new project from template

    :param project_name:
    :return:
    '''
    subprocess_run("cp -r "+labkit_dir+"/template/workplace/data/example ./"+project_name)


@register
def calc(calc_name):
    '''
    calculate project, input yml file

    :param calc_name:
    :return:
    '''
    # todo: 计算yaml和当前文件夹.
    # subprocess_run("cp -r "+labkit_dir+"/template/workplace/data/result ./")
    
    pass

@register
def new_module(module_name):
    '''
    new module from template

    :param module_name:
    :return:
    '''
    subprocess_run("cp -r "+labkit_dir+"/template/module/new_module.py "+module_name+".py")



def cli():
    # alternative分派, 默认分派是函数名, 用字典可以修改默认分派名, 用@kwoargs可以对关键字参数进行分派
    # run(hello_world,alt={"vvv":version, "no_capitalized":hello_world})

    # 分派必须显示说明, 可以传入列表
    description="""
    labkit cli interface
    """
    commands=_functions
    run(commands,description=description)


if __name__ == '__main__':
    cli()




