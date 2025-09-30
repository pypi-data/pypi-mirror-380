#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

# import importlib
from __future__ import print_function
import os
import re
import sys

from general import gs
from general.reflection import get_script_location

from vi.interpreter.loaders import call, load_yaml_file, load_module
from vi.interpreter.context import get_context,set_context,update_context

log=gs.get_logger(__name__,debug=True)

# filename=sys.argv[1]

# 本地执行, 不推送到队列, 可以测试和调试用. todo:已经合并eval_tree_local和eval_tree两个函数. 在eval_tree调试好之后删除.
def eval_tree_local(tree):
    '''
    parse a conf(dict) and run it

    :param tree:
    '''

    # print type(conf)
    # 如果什么都不是则返回自身
    if type(tree)!=dict and type(tree)!=list:
        if load_module(tree):
            # return conf
            return call(tree,{})
        else:
            return tree
    # 如果是list则递归解析
    if type(tree)==list:
        ans=[]
        for item in tree:
            # print item
            ans.append(eval_tree(item))
        return ans
    # 如果是dict递归解析, 如果key是module, 执行
    else:
        ans={}

        # 分类讨论repeat和until
        if 'repeat' in tree:
            repeat=tree['repeat']
            if 'until' in tree:
                until=tree['until']
            else:
                until=False
        elif 'until' in tree:
            repeat=1000000
            until=tree['until']
        else:
            repeat=1
            until=True

        # until=conf.get('until',True)
        # repeat=conf.get('repeat',1)

        for loop in range(repeat):
            for key in tree.keys():
                child=tree[key]
                # print key, child

                # if type(child)!=dict and type(child)!=list:
                    # print child
                    # ans.update({key,child})
                    # return child
                # if type(child)==list:
                    # ans.update(key,run(child))
                # else:
                if load_module(key):
                    print(key ,child)
                    # print call(key,parse(child))

                    return call(key,eval_tree(child))
                    # ans.update({key:call(key,eval_conf(child))})

                else:
                    ans.update({key:eval_tree(child)})
            until=eval_tree(until)
            if until:
                break

        return ans


# Ensemble方式处理, 采用数据库
# from vi.parallel.mapreduce import deal_with_line

# todo: 此处正在用来切换使用local
deal_with_line=call

# 文件方式处理

def eval_tree(tree):
    '''
    parse a conf(dict) and run it

    :param tree:
    :return:
    '''

    # print type(conf)
    # 如果什么都不是则返回自身
    if type(tree)!=dict and type(tree)!=list:
        if load_module(tree):
            # return conf
            # return call(tree,{})
            # 求值, 如果没有参数也执行, 返回执行结果
            return deal_with_line(tree,{})

        else:
            return tree
    # 如果是list则递归解析
    if type(tree)==list:
        ans=[]
        for item in tree:
            # print item
            ans.append(eval_tree(item))
        return ans
    # 如果是dict递归解析, 如果key是module, 执行
    else:
        ans={}

        # 分类讨论repeat和until
        if 'repeat' in tree:
            repeat=tree['repeat']
            if 'until' in tree:
                until=tree['until']
            else:
                until=False
        elif 'until' in tree:
            # until迭代最大次数. todo:可以配置. 此外repeat和until还需再审核
            repeat=1000000
            until=tree['until']
        else:
            repeat=1
            until=True

        for loop in range(repeat):
            for key in tree.keys():
                child=tree[key]
                if load_module(key):
                    print (key ,child)
                    # 主动的推送
                    # return call(key,eval_tree(child))
                    # 自动的推送
                    return deal_with_line(key,eval_tree(child))


                else:
                    # 用一般参数更新context
                    # todo: 此处也应该是update_context({key:eval_tree(child)}, ans和返回值还需审核
                    if type(child)!=dict and type(child)!=list:
                        update_context({key:child})

                    # path 放在参数里面 todo:这里和eval_tree_local不一样, 修正
                    ans.update({key:eval_tree(child)})
            until=eval_tree(until)
            if until:
                break

        return ans


def run_yaml_file(input_element):
    '''
    run a yml file. parse the file to dict and run it

    :param filename:
    :return:
    '''
    filename=input_element['filename']
    algorithm= load_yaml_file(filename)

    # 开始和结束都重置context todo: 应该要重置的, 断点续运行的问题.
    # set_context({})

    ans=eval_tree(algorithm)
    print (ans)

    # set_context({})

    return ans


def run(input_element, args={}):
    run_yaml_file(input_element)
    return True

def selfrun(input_element={},args={}):
    import vi.init_gs
    from vi.interpreter.loaders import call_by_filename
    call_by_filename(__file__, input_element, args)
if __name__ == '__main__':
    selfrun(args={'filename':'hello.yml'})

