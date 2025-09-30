#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


import pymongo
from general import gs
from general import gs
from general.unit import hartree_to_kcal
from pymongo import MongoClient

from ms.conformer import Conformer

log=gs.get_logger(__name__,debug=False)

from vi.interpreter.context import get_context, update_context

OPTS = [
    gs.cfg.FloatOpt('energy_cut',
                    default=30,
                    help='pool energy cut for conformer'),
]

gs.CONF.register_opts(OPTS)

import beanstalkc
import time
# import labkit.init_gs

bq = beanstalkc.Connection(host=gs.CONF.beanstalk_server, port=gs.CONF.beanstalk_port)

import json
class Ensemble2(object):
    '''
    ensemble 是 collection级别的
    '''
    def __init__(self, db_name="labkit", collection_name="default"):
        self.client = MongoClient(host=gs.CONF.mongo_server, port=gs.CONF.mongo_port)
        self.db=self.client[db_name]
        self.collection=self.db[collection_name]
        self.bq = beanstalkc.Connection(host=gs.CONF.beanstalk_server, port=gs.CONF.beanstalk_port)
        self.bq.use('compute')
        # self.index()

    ### ============ 数据库相关操作


    def save(self,conformer):
        '''
        save a conformer to the ensemble.

        :param conformer:
        :return:  return True is conformer is needed and saved, False if conformer is excluded.
        '''

        # self.collection.insert_one(conformer.to_dict())
        # return True

        # todo: 修复build的时候pdb两个H的问题.
        if self.need_conformer(conformer):
            self.collection.insert_one(conformer.to_dict())
            return True
        else:
            return False

    def index(self):
        '''
        create index for energy.
        index being created only once is ok.

        :return:
        '''
        return self.collection.create_index([('energy', pymongo.ASCENDING)])
        # print((self.collection.index_information()))
        # print(list(self.collection.index_information()))


    def find_one(self):
        # done: 这里很有用, 可以抽象, db.name, collection.name 是db和collection相应的名字
        return Conformer().from_dict(self.collection.find_one())

    def find(self):
        return self.collection.find()


    # 函数式操作, map, filter, reduce

    def map(self,module_name,args):
        # map a ensembel to another ensemble with module_name's run function
        all=self.find()

        task={}
        task['module_name']=module_name
        args.update(get_context())
        task['args']=args
        self.bq.use('compute')

        # 取出ensemble所有构型
        # ensemble_name=args['ensemble']
        # 应用单体命令

        for i in all:
            task['args']['xyz']=i['xyz']
            task['args']['code']=i['code']
            task['args']['current_ensemble']=args['current_ensemble']
            print task
            self.bq.put(json.dumps(task))

        # todo: 等待处理完成
        while bq.stats_tube('compute')['current-jobs-ready']!=0 or bq.stats_tube('compute')['current-jobs-reserved']!=0 :
            time.sleep(1)

        # todo: 刷新context
        # context=get_context()
        # context['running_job']
        update_context({'last_ensemble':args['current_ensemble']})

    def filter(self,module_name,args):
        pass

    def reduce(self,module_name,args):
        pass


