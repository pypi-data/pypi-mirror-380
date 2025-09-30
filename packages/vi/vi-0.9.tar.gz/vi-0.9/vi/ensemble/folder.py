#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry
from vi.ensemble.base import BaseEnsemble



from general.cli import subprocess_run
import subprocess

import os, glob
from general import gs


# todo: 解决文件和文件名接口的转换问题. 是不是用装饰器呢.
def call_by_filename(input_filename, command):
    subprocess_run(command + ' ' + input_filename)



# todo:组装.

# todo: 给wrapper找个好地方放
def wrapper(parameters):
    def function(func):
        def wrap_func(*element):
            # print parameters
            return func(*element, parameters=parameters)

        return wrap_func

    return function


class FolderVector():
    def __init__(self, folder_name='.'):
        # self.location
        self.folder_name = folder_name
        # self.current_vector = folder_name

    def find(self):
        return self.vector_iterator_of_files(self.folder_name)

    @staticmethod
    def generate_next_foldername(foldername, func_name):
        base = os.path.basename(foldername)
        dirname = os.path.dirname(foldername)
        s = base.split(',')
        s[1] = str(int(s[1]) + 1)
        s[2] = func_name
        return os.path.join(dirname, ','.join(s))

    # todo: 改推送
    def map_old(self, func, args={}):
        function = wrapper(args)(func)
        new_folder_name = self.generate_next_foldername(self.folder_name, func.func_name)
        try:
            os.mkdir(new_folder_name)
        except:
            if (gs.CONF.overwrite == True):
                pass
            else:
                raise
        # done: 有目录存在的时候, 使用gs.CONF.overwrite选项控制是否覆盖. overwrite==True的时候, 覆盖不抛出异常.

        for i in self.find():
            output = function(i)
            file_name = os.path.basename(i)
            output_filename = os.path.join(new_folder_name, file_name)
            # print output_filename
            output_file = open(output_filename, 'w')
            output_file.write(output)
            output_file.close()
        new_folder = FolderVector(new_folder_name)
        return new_folder
        # return map(function, self.find())

    def map(self, func, args={}):
        function = wrapper(args)(func)
        new_folder_name = self.generate_next_foldername(self.folder_name, func.func_name)
        try:
            os.mkdir(new_folder_name)
        except:
            if (gs.CONF.overwrite == True):
                pass
            else:
                raise
        # done: 有目录存在的时候, 使用gs.CONF.overwrite选项控制是否覆盖. overwrite==True的时候, 覆盖不抛出异常.

        for i in self.find():
            output = function(i)
            file_name = os.path.basename(i)
            output_filename = os.path.join(new_folder_name, file_name)
            # print output_filename
            output_file = open(output_filename, 'w')
            output_file.write(output)
            output_file.close()
        new_folder = FolderVector(new_folder_name)
        return new_folder
        # return map(function, self.find())

    # todo: 改造filter和reduce
    def filter(self, func, arg={}):
        function = wrapper(arg)(func)
        return filter(function, self.current_vector)

    def reduce(self, func, arg={}):
        function = wrapper(arg)(func)
        return [reduce(function, self.current_vector)]

    def sort(self):
        self.current_vector[:] = sorted(self.current_vector)[:]
        return self.current_vector

    def deduplicate(self):
        self.current_vector[:] = list(set(self.current_vector))[:]
        return self.sort()

    # todo: suffix 变动
    @staticmethod
    def vector_iterator_of_files(folder='.', suffix='*.xyz'):
        base_abspath = os.path.abspath(folder)
        return glob.iglob(os.path.join(base_abspath, suffix))


class ListEnsemble(BaseEnsemble):
    def __init__(self, vector):
        self.context = {}
        self.ensemble = []

        self.current_vector = vector
        # todo: 把ensemble改成[(vector, context)...]的形式. context指明vector存储的位置.
        self.ensemble.append(self.current_vector)

    def next(self, func, args={}):
        # todo: map返回的是列表, 但是vector不是列表. 而是一个新的vector. 重要! 是否需要返回新的vector.
        self.ensemble.append(self.get_last_vector().map(func, args))

    def get_last_vector(self):
        return self.ensemble[-1]

    def new_vector(self):
        return

    def put_back(self):
        """
        运算结束后如何放回.  map, reduce, filter应该是不一样的行为.
        :return:
        """
        return


def square(x, args={}):
    return x * x


def add(x, y, args={}):
    return x + y


def test2():
    l = FolderVector([1, 2, 3, 2])
    print l.sort()
    print l.current_vector
    print l.deduplicate()
    print l.map(square)
    print l.map(square, args={})
    print l.filter(lambda x, args={}: x > 2)
    print l.current_vector
    print l.reduce(add, arg={})
    print l.find()
    print list(l.find())

    e = ListEnsemble(l)
    # print e.get_last_vector().current_vector
    print e.ensemble
    e.next(square, {})
    print e.ensemble
    # print e.get_last_vector().current_vector

    # s = [1, 2, 3, 2]
    # s.sort(lambda x, y: x if x < y else y)
    # print sorted(s)


if __name__ == '__main__':
    import vi.init_gs

    test()
