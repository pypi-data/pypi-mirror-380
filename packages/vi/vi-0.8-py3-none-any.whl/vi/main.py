#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

from clize import run
from vi.algorithm.ga.cga import cga_run

from vi import check_config


def main():
    # 循环config

    for turn in check_config.RUN:
        SAMPLE_METHOD = turn['SAMPLE_METHOD']
        algorithm = turn['SAMPLE_METHOD']['ALGORITHM']
        constraned = turn['SAMPLE_METHOD']['CONSTRANED']
        meta_method = turn['META_METHOD']

        if algorithm == 'SYS':
            cga_run()
        elif algorithm=='GA':
            cga_run()





if __name__ == '__main__':
    run(main)
