#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


import unittest
from general import gs
from vi.interpreter import loaders
import vi.init_gs


class TestLoaders(unittest.TestCase):
    def setUp(self):

        pass

    def tearDown(self):
        pass

    def test_load_yaml_file(self):
        filename = 'test.yml'
        loaders.load_yaml_file(filename)
        return

    def test_load_parameters(self):
        print loaders.load_parameters()



    def test_run(self):
        return
        loaders.run(conf)

    def test_load_module(self):
        self.assertEqual(loaders.load_module('sys'), None)
        self.assertEqual(type(loaders.load_module('ms.simple.square')), type(unittest))
        return

    def test_load_args(self):
        libname='ms.simple.square'
        return loaders.load_args(libname, new_args={'arg3':3})

    def test_load_self_args(self):
        return
        loaders.load_args_by_self_file(filename, args={})

    def test_load_args_by_filename(self):

        return
        loaders.load_args_by_filename(filename)

    def test_filename_to_module_name(self):

        module_name='ms.simple.square'
        filename=loaders.module_name_to_file_name(module_name)
        self.assertEqual(loaders.filename_to_module_name(filename), 'ms.simple.square')
        self.assertEqual(loaders.filename_to_module_name('jjojo'), None)


        return
    def test_module_name_to_file_name(self):

        module_name='ms.simple.square'
        return loaders.module_name_to_file_name(module_name)

    def test_call(self):
        return
        loaders.call(libname, input_element, args)

    def test_callrun(self):
        return
        loaders.call_by_filename(filename, input_element={})


if __name__ == '__main__':
    unittest.main()
