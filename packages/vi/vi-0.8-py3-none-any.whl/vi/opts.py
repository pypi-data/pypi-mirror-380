#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


import itertools


def list_opts():
    return [
        ('DEFAULT',
         itertools.chain(vi.OPTS,
                         vi.OPTS, )),
        ('api',
         itertools.chain(vi.api.OPTS,
                         [vi.API_OPT])),
        ]
# list_opts()
