#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


import unittest

from vi.cmd import labkit


class TestLabkit(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_service(self):
        return
        labkit.service(command)

    def test_new(self):
        return
        labkit.new(project_name)

    def test_calc(self):
        return
        labkit.calc(calc_name)

    def test_new_module(self):
        return
        labkit.new_module(module_name)

    def test_cli(self):
        return
        labkit.cli()


if __name__ == '__main__':
    unittest.main()
