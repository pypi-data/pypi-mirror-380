#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry
'''
载入yamlfile, module, args, 以及call module

'''
import importlib
# from __future__ import print_function
import os,re
import jinja2
import yaml

from general import gs
from general.reflection import get_script_location

log=gs.get_logger(__name__,debug=True)

self_location = get_script_location(__file__)

def load_yaml_file(filename):
    '''
    根据文件名加载yml配置文件, 先调用jinja模板渲染, 然后再解析. 最后返回解析后的字典.
    :param filename: 配置文件名
    :return: 解析后的字典
    '''
    f=open(filename,'r')
    # rendered= jinja2.Template(f.read()).render(jinja='jinjia2')
    rendered=f.read()
    tree=yaml.load(rendered)
    return tree

def make_template():
    pass

def load_parameters():
    '''
    遍历载入所有模块的参数
    :return:
    '''
    # folder=[gs.CONF.packages_folder,gs.CONF.local_packages_folder]
    # os.walk()

    # todo: bugfix 处理文件夹加__init__.py的形式.

    #  config 是一个模块对象, 里面包含所有全局配置的变量. 用check_config加载
    # config.check_config('config.yml')
    # package_dir=config.project['name']

    ans={'all_parameters':{}}
    folder=gs.CONF.packages_folder
    packages_folder=map(lambda x:os.path.join(folder,x),os.listdir(folder))
    folder=gs.CONF.local_packages_folder
    local_packages_folder=map(lambda x:os.path.join(folder,x),os.listdir(folder))
    walk_through_folder=packages_folder+local_packages_folder
    log.debug("walk_through_folder:" + str(walk_through_folder))
    for package_dir in walk_through_folder:
        exclude_dir=set(['tests','target','template','__pycache__'])
        py_pattern=re.compile(r'^(?!__init__).*\.py$')
        replace_pattern=re.compile(r'^%s'%package_dir)
        for root,dirs,files in os.walk(package_dir,topdown=True):
            # 本地修改, 另外列表生成式里面的变量不是局域的, 在用完后会保留.
            dirs[:] = [d for d in dirs if d not in exclude_dir]
            files[:] = [f for f in files if py_pattern.match(f)]
            for file in files:
                py_file=os.path.join(root,file)

                definition_pattern=re.compile(r'^parameters.*=.*$',re.M)
                with open(py_file) as f:
                    content=f.read()

                have_parameters=definition_pattern.search(content)
                if have_parameters:
                    module_name=filename_to_module_name(py_file)
                    module=load_module(module_name)
                    ans['all_parameters'][module_name]=module.parameters

    return ans



# ========== 载入module和args相关 ============
# ROOT
# 可以使用import module & inspect 的方法获取func_name和func_definition

def load_module(module_name):
    '''
    load a module by lib name
    :param module_name:
    :return: return the module object
    '''

    file_name=module_name_to_file_name(module_name)
    if not file_name: return None

    try:
        # 暂时不允许使用root包以外的模块, 否则容易冲突.
        if module_name == 'vi.interpreter.runner':
            lib=importlib.import_module(module_name)
            return lib
        else:
            raise ImportError
        # lib.run(load(i+'.yml'))
    except:
        try:
            # todo: 直接使用会冲突, 要限定范围
            # name=gs.CONF.self_package_name+'.'+name

            # 判断packages文件夹下, 模块是否存在, 不存在则忽略
            # 存在, 判断是否有definition, 没有, 抛出异常, 有则导入

            log.debug("module name is: " + module_name)
            lib=importlib.import_module(module_name)
            return lib
        except:
            raise ImportError


def load_args(module_name, new_args={}):
    '''
    load conf by lib name
    优先加载当前目录下的module_settings, 否则加载默认的. args用来更新.
    :param module_name:
    :param new_args:
    :return: the module args
    '''

    conf={}
    root=gs.CONF.packages_folder

    module=load_module(module_name)
    conf.update(module.parameters)
    conf.update(get_context())
    conf.update(new_args)
    return conf

    module_setting_folder_name='module_settings'
    try:
        if os.path.exists(module_setting_folder_name) and os.path.isdir(module_setting_folder_name):
            conf_file=os.path.join(module_setting_folder_name, module_name + '.yml')
            conf=load_yaml_file(conf_file)
        elif os.path.exists(os.path.join(root,module_setting_folder_name)) and os.path.isdir(os.path.join(root,module_setting_folder_name)):
            conf_file=os.path.join(root, module_setting_folder_name, module_name + '.yml')
            log.debug("conf_file is: "+conf_file)
            conf=load_yaml_file(conf_file)
    except:
        pass
    finally:
        conf.update(new_args)

    return conf

def load_args_by_self_file(filename, args={}):
    '''
    filename should be __file__
    in a module itself, load conf by the arguments __file__
    same with load_conf_by_filename, but this is special for a in-module self load.
    :param filename:
    :return:
    '''
    # print os.path.realpath(filename)
    # print get_module_name(os.path.realpath(filename))
    return load_args(filename_to_module_name(os.path.realpath(filename)))


def load_args_by_filename(filename):
    '''
    load_conf's arg is lib name, this function can load conf by filename
    :param filename:
    :return:
    '''
    return load_args(filename_to_module_name(filename))

# labkit_dir='/Users/lhr/@core/_action/labkit/packages/ms'

def filename_to_module_name(filename):
    '''
    get module/lib name by filename
    :param filename:
    :return:
    '''
    try:
        module_name=filename
        # todo: 优化路径的设置, 以及检查出错, 只允许使用packages里面的包


        root=gs.CONF.local_packages_folder
        splited=module_name.split(root+'/')
        if len(splited)==1:
            root=gs.CONF.packages_folder
            splited=module_name.split(root+'/')

        log.debug("splited is: "+str(splited))
        ans= splited[-1].split('/')
        ans=ans[1:]
        ans[-1]=ans[-1].replace('.pyc','')
        ans[-1]=ans[-1].replace('.py','')
        ans='.'.join(ans)
        return ans
    except:
        return None
def module_name_to_file_name(module_name):
    '''
    convert a module name to file name, if module not exist, return None.
    :param module_name:
    :return:
    '''

    # done: 优化路径的设置, 以及检查出错, 只允许使用packages里面的包
    packages_folder=gs.CONF.packages_folder
    local_packages_folder=gs.CONF.local_packages_folder

    # todo: 现在是一一对应关系, 以后可以允许时候用egg包
    filename=apply(os.path.join,[packages_folder]+[module_name.split('.')[0]]+module_name.split('.'))+'.py'

    local_filename=apply(os.path.join,[local_packages_folder]+[module_name.split('.')[0]]+module_name.split('.'))+'.py'

    if os.path.exists(local_filename):
        return local_filename
    elif os.path.exists(filename):
        return filename
    else:
        return None


# ===========  运行载入的module, call(module, element, args) ========

from vi.interpreter.context import get_context

# ----------
def call(module_name, input_element, args):
    '''
    call a lib's run function with args.
    根据模块名字调用模块的run函数, 并且加载同名配置文件, 并合并传入的参数

    :param module_name: 模块名
    :param input_element: 输入元素, dict
    :param args: 传入的参数字典, dict
    :return: 模块run函数的返回值
    '''

    # todo: 测试使用load_module
    # lib=load_module(libname)
    # print os.environ['PYTHONPATH']
    # import simple.square
    lib=importlib.import_module(module_name)

    # 用context更新args, 在push_to_compute里面更新
    # args.update(get_context())
    # print get_context()

    # 用args更新conf  todo: 处理args和conf
    # conf=load_conf(libname,args)


    # print (conf)
    log.info("calling %s..." % module_name)
    # print (lib)
    # todo: 把run改成single_func. 不要改.
    # func_name=lib.difinition['single_func']

    return lib.run(input_element,args)





def call_by_filename(filename, input_element={}, args={}):
    '''
    in a module itself, call the 'run' entry point in the argument 'filename', __file__
    根据__file__得到脚本的模块名字. 然后用call调用它.
    :param filename: full file path and name, please simplely use __file__
    :param input_element:
    :return:
    '''
    current_module_name=filename_to_module_name(filename)
    # print current_module_name
    # print input_element
    log.debug("current module name is: "+current_module_name)
    call(current_module_name, input_element,args)


def run(args):
    '''
    run必须有一个参数conf, 作为传入的配置.
    run是模块的入口
    :param args: 参数字典
    :return: run的返回值
    '''
    print("hello world this is loader")



if __name__ == '__main__':
    import vi.init_gs
    # from vi.interpreter.loader import callrun
    # print gs.CONF.self_package_name
    # print __file__
    # call_by_filename(__file__)
    # todo: 在外面调用可以, 在本文件调用则不行. 待查明.
    ans=load_parameters()
    print ans
