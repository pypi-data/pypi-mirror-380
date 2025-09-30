#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


import unittest

from vi.interpreter import runner


class TestRunner(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_eval_tree(self):
        return
        runner.eval_tree(tree)

    def test_run_file(self):
        runner.run_yaml_file(args)

    def test_run(self):
        return
        runner.run(args)

    def test_selfrun(self):
        return
        runner.selfrun(args={})


if __name__ == '__main__':
    unittest.main()
