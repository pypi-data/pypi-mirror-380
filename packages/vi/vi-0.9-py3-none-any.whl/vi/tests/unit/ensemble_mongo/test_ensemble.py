#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


import unittest

from vi.ensemble_mongo import ensemble


class TestEnsemble(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test___init__(self):
        return
        ensemble.__init__(self, db_name="labkit", collection_name="default")

    def test_save(self):
        return
        ensemble.save(self, conformer)

    def test_index(self):
        return
        ensemble.index(self)

    def test_get_father(self):
        return
        ensemble.get_father(self, conformer)

    def test_find_one(self):
        return
        ensemble.find_one(self)

    def test_find(self):
        return
        ensemble.find(self)

    def test_find_by_conformer(self):
        return
        ensemble.find_by_conformer(self, *args, **kwargs)

    def test_find_top_energy(self):
        return
        ensemble.find_top_energy(self, count)

    def test_min_energy(self):
        return
        ensemble.min_energy(self)

    def test_map(self):
        return
        ensemble.map(self, module_name, args)

    def test_filter(self):
        return
        ensemble.filter(self, module_name, args)

    def test_reduce(self):
        return
        ensemble.reduce(self, module_name, args)

    def test_is_needed_in_pool(self):
        return
        ensemble.is_needed_in_pool(self, energy_cut=gs.CONF.energy_cut)

    def test_needed_conformer_2(self):
        return
        ensemble.needed_conformer_2(self, conformer, rmsd_range=gs.CONF.rmsd_range, energy_cut=gs.CONF.energy_cut)

    def test_duplicated_conformer(self):
        return
        ensemble.duplicated_conformer(self, conformer, rmsd_range=gs.CONF.rmsd_range)

    def test_cut_conformer(self):
        return
        ensemble.cut_conformer(self, conformer, energy_cut=gs.CONF.energy_cut)

    def test_need_conformer(self):
        return
        ensemble.need_conformer(self, conformer, rmsd_range=gs.CONF.rmsd_range, energy_cut=gs.CONF.energy_cut)

    def test_test(self):
        return
        ensemble.test()

    def test_run(self):
        return
        ensemble.run(args)


if __name__ == '__main__':
    unittest.main()
