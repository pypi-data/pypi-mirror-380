#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


import unittest

from vi.interpreter import context


class TestContext(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_context(self):
        return
        context.get_context()

    def test_update_context(self):
        return
        context.update_context(conf)

    def test_set_context(self):
        return
        context.set_context(context)

    def test_test(self):
        return
        context.test()

    def test_run(self):
        return
        context.run(conf)

    def test_selfrun(self):
        return
        context.selfrun()


if __name__ == '__main__':
    unittest.main()
