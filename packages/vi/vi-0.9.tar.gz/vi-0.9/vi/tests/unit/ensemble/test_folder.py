#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

import unittest
from unittest import TestCase
from vi.ensemble.folder import FolderVector,ListEnsemble
from simple.cat import cat_by_filename,run
#import pytest


class TestFolderVector(unittest.TestCase):
    def setUp(self):
        self.l = FolderVector('./ensemble/gen,1,init')

    def test_find(self):
        print list(self.l.find())

    def test_generate_foldername(self):
        self.fail()

    def test_map(self):
        print self.l.map(cat_by_filename)

    def test_filter(self):
        assert 1==2
        # self.fail()

    def test_reduce(self):
        self.fail()

    def test_sort(self):
        self.fail()

    def test_deduplicate(self):
        self.fail()

    def test_vector_iterator_of_files(self):
        self.fail()


class TestListEnsemble(TestCase):

    def setUp(self):
        self.l = FolderVector('./ensemble/gen,1,init')
        self.e = ListEnsemble(self.l)

    def test_next(self):
        # self.e.next(cat_by_filename)
        # print list(self.e.get_last_vector().find())

        self.e.next(run,args={'hello': 'world'})
        print self.e.get_last_vector()

        # self.e.next(cat_by_filename, parameters={'hello': "world"})
        # print self.e.get_last_vector()



def test_get_last_vector(self):
        print self.e.get_last_vector()

if __name__ == '__main__':
    unittest.main()

