#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

# must only be imported to introduce the globle configures. because the __file__ variable identified the location of the configured package.

from general import gs
log=gs.get_logger(__name__,debug=False)

from general.gs import cfg,types
PortType = types.Integer(1, 65535)


OPTS = [
    cfg.StrOpt('redis_server',
               default='localhost',
               help='redis server to connect  to '),
    cfg.Opt('redis_port',
            type=PortType,
            default=6379,
            help='redis port number to connect to'),
    cfg.StrOpt('beanstalk_server',
               default='localhost',
               help='beanstalk server to connect  to '),
    cfg.Opt('beanstalk_port',
            type=PortType,
            default=11300,
            help='beanstalk port number to connect to'),
    cfg.StrOpt('mongo_server',
               default='localhost',
               help='mongo server to connect  to '),
    cfg.Opt('mongo_port',
            type=PortType,
            default=27017,
            help='mongo port number to connect to'),

    cfg.StrOpt('dbname',
            default="labkit",
            help='dbname in mongdb'),

    cfg.BoolOpt('overwrite',
                default=True,
                help='overwrite folder toggle')

    ]


gs.init(__file__,OPTS)

# log=gs.get_logger(__name__,debug=gs.CONF.debug)

log.debug("gs loaded, root is "+gs.CONF.self_package_name)
