#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

from vi.ensemble.base import BaseEnsemble
# 接口
# func(element, args)
# call(func/module_name,element,args)
# task[ module_name, element, args ]
# context作为Ensemble的常量, 在运行的时候用.
#
# 上级调用的时候, 只要接口, 而不管存储形式.  返回值应该都是vector迭代器.


def wrapper(parameters):
    def function(func):
        def wrap_func(*element):
            return func(*element, args=parameters)
        return wrap_func
    return function


class ListVector():
    def __init__(self, alist=[]):
        # self.location
        self.current_vector = alist

    def find(self):
        return iter(self.current_vector)

    def map(self, func, arg={}):
        # 按照map推送队列,
        function=wrapper(arg)(func)
        return map(function, self.current_vector)

    def filter(self, func,arg={}):
        # function=lambda element:func(element,arg)
        function=wrapper(arg)(func)
        return filter(function, self.current_vector)

    def reduce(self, func,arg={}):
        # function=lambda element:func(element,arg)
        function=wrapper(arg)(func)
        return [reduce(function, self.current_vector)]
        # 结束后放回
        # self.ensemble.append(next_vector)
        # self.current_vector = next_vector
    def sort(self):
        # 如何排序
        self.current_vector[:] = sorted(self.current_vector)[:]
        return self.current_vector

    def deduplicate(self):
        # 去重
        # self.current_vector()
        self.current_vector[:] = list(set(self.current_vector))[:]
        return self.sort()


class ListEnsemble(BaseEnsemble):
    def __init__(self, vector):
        self.context = {}
        self.ensemble = []

        self.current_vector = vector
        # todo: 把ensemble改成[(vector, context)...]的形式. context指明vector存储的位置.
        self.ensemble.append(self.current_vector)

        # self.sort()

        # self.type='folder'
        # self.location='foder position'
        # self.get=(...)
        #
        # {
        #     type: folder, database
        #     location: 'location'
        # get
        # }


        # self.next_vector=[]

    def next(self, func, arg={}):
        # todo: map返回的是列表, 但是vector不是列表. 而是一个新的vector. 重要! 是否需要返回新的vector.
        self.ensemble.append(self.get_last_vector().map(func, arg))

    def get_last_vector(self):
        return self.ensemble[-1]

    def find(self):
        """
        找出所有的元素
        :return:
        """
        # print self.current_vector
        return iter(self.current_vector)

    def new_vector(self):
        return

    def put_back(self):
        """
        运算结束后如何放回.  map, reduce, filter应该是不一样的行为.
        :return:
        """
        return



def square(x,args={}):
    return x * x


def add(x, y,args={}):
    return x + y


# print wrapper("")(square)(2)
# exit(0)


if __name__ == '__main__':
    l = ListVector([1, 2, 3, 2])
    print l.sort()
    print l.current_vector
    print l.deduplicate()
    print l.map(square)
    print l.map(square,arg={})
    print l.filter(lambda x,args={}: x > 2)
    print l.current_vector
    print l.reduce(add,arg={})
    print l.find()
    print list(l.find())

    e=ListEnsemble(l)
    # print e.get_last_vector().current_vector
    print e.ensemble
    e.next(square,{})
    print e.ensemble
    # print e.get_last_vector().current_vector

    # s = [1, 2, 3, 2]
    # s.sort(lambda x, y: x if x < y else y)
    # print sorted(s)
