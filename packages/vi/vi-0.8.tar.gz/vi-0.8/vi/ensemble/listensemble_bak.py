#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

from vi.ensemble.base import BaseEnsemble


# 上级调用的时候, 只要接口, 而不管存储形式.  返回值应该都是vector迭代器.

class ListVector():
    def __init__(self, alist=[]):
        # self.location
        self.vector = alist

    def find(self):
        return iter(self.current_vector)

    def map(self, func, arg):
        # 按照map推送队列,
        next_vector = map(func, self.current_vector)
        # 结束后放回
        self.ensemble.append(next_vector)
        self.current_vector = next_vector

    def reduce(self, func):
        next_vector = [reduce(func, self.current_vector)]
        # 结束后放回

        self.ensemble.append(next_vector)
        self.current_vector = next_vector

    def filter(self, func):
        next_vector = filter(func, self.current_vector)

        # 结束后放回
        self.ensemble.append(next_vector)
        self.current_vector = next_vector
        self.sort()


class ListEnsemble(BaseEnsemble):
    def __init__(self, vector):
        self.context = {}
        self.ensemble = []

        self.current_vector = vector
        # todo: 把ensemble改成[(vector, context)...]的形式. context指明vector存储的位置.
        self.ensemble.append(self.current_vector)
        self.sort()

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

    def next(self, func, arg):
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

    def sort(self):
        # 如何排序
        self.current_vector[:] = sorted(self.current_vector)[:]

    def deduplicate(self):
        # 去重
        # self.current_vector()
        return


def square(x):
    return x * x


def add(x, y):
    return x + y


if __name__ == '__main__':
    l = ListEnsemble([1, 2, 3, 2])
    print l.find()
    print l.ensemble
    l.map(square)
    l.map(square)
    l.filter(lambda x: x > 2)
    l.reduce(add)
    print l.ensemble
    print l.find()

    s = [1, 2, 3, 2]
    s.sort(lambda x, y: x if x < y else y)
    print sorted(s)
