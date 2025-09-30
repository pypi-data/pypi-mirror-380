#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

class BaseEnsemble(object):
    def __init__(self):
        pass

    def map(self):
        raise "please implement map function"


    def reduce(self):
        raise "please implement reduce function"

    def filter(self):
        raise "please implement filter function"

    def sort(self):
        raise "please implement sort function"
    def deduplicate(self):
        raise "please implement deduplicate function"



# e=Ensemble()

if __name__ == '__main__':
    pass



