#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


import unittest

from vi.cmd import labkit_manage


class TestCli_inside(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_push(self):
        return
        labkit_manage.push(yml_file='task.yml')

    def test_kick(self):
        return
        labkit_manage.kick()

    def test_worker(self):
        return
        labkit_manage.worker(queue_names='compute')

    def test_front(self):
        return
        labkit_manage.front(queue_names='tasks')

    def test_rest(self):
        return
        labkit_manage.rest()

    def test_start(self):
        return
        labkit_manage.start()

    def test_startdb(self):
        return
        labkit_manage.startdb()

    def test_backup_beanstalk(self):
        return
        labkit_manage.backup_beanstalk(beanstalk_dir)

    def test_restore_beanstalk(self):
        return
        labkit_manage.restore_beanstalk(beanstalk_dir)

    def test_backup_mongo(self):
        return
        labkit_manage.backup_mongo()

    def test_restore_mongo(self):
        return
        labkit_manage.restore_mongo()

    def test_backup(self):
        return
        labkit_manage.backup()

    def test_restore(self):
        return
        labkit_manage.restore()

    def test_cli(self):
        return
        labkit_manage.cli()


if __name__ == '__main__':
    unittest.main()
