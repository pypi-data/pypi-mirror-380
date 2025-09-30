#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

'''
处理单行, 解构Ensemble, 根据单体函数和map, reduce属性, 生成并行化代码并push到队列.
'''


from vi.scheduler.push import bq
import  time
from vi.ensemble_mongo.ensemble import Ensemble


def deal_with_line(module_name, args):
    '''
    对于compute中的模块调用map, 推送队列
    对于filter中的模块调用filter
    其他的就直接执行

    :param module_name:
    :param args:
    :return:
    '''
    args.update(get_context())
    log.debug(args)

    if 'compute' in module_name:
        log.debug(module_name)
        log.debug(module_name)
        args['current_ensemble']=args['ensemble_name']+'_'+module_name.replace('.','_')
        if 'gaussian' in module_name:
            args['current_ensemble']+='_'+args['method'].replace('/','_').replace(' ', '_')

        log.debug(args['current_ensemble'])
        ensemble=Ensemble(collection_name=args['last_ensemble'])

        ensemble.map(module_name,args)



    elif 'filter' in module_name:
        collection_name=args['ensemble']+'_'+module_name.replace('.','_')
        ensemble=Ensemble(collection_name=collection_name)
        ensemble.filter(module_name,args)
    else:
        call(module_name,args)

    return True

    task={}
    task['module_name']=module_name
    args.update(get_context())
    task['args']=args
    bq.use('compute')
    # 取出ensemble所有构型
    # ensemble_name=args['ensemble']
    # 应用单体命令
    bq.put(json.dumps(task))
    # todo: 等待处理完成
    while bq.stats_tube('compute')['current-jobs-ready']!=0 or bq.stats_tube('compute')['current-jobs-reserved']!=0 :
        time.sleep(1)
    # todo: 刷新context
    # context=get_context()
    # context['running_job']
    return True



def push():
    pass

def map():
    pass
def reduce():
    pass

if __name__ == '__main__':
    pass


