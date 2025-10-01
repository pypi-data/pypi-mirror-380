# Copyright 2016 to 2021, Cisco Systems, Inc., all rights reserved.
"""Tests for yscoverage.yangdiff module."""

import os
import unittest

from yscoverage.yangdiff import getdiff
from yscoverage.dataset import dataset_for_yangset
from yangsuite.paths import set_base_path


class TestYangDiff(unittest.TestCase):

    testdir = os.path.join(os.path.dirname(__file__), 'data')

    def setUp(self):
        set_base_path(self.testdir)

    def test_diff_openconfig_interfaces_basic(self):
        fromdata = dataset_for_yangset('test', 'ocif-alpha',
                                       'openconfig-interfaces', ['nodetype'])
        todata = dataset_for_yangset('test', 'ocif-beta',
                                     'openconfig-interfaces', ['nodetype'])
        result = getdiff(fromdata, todata)
        print(result['header'])
        self.assertEqual(['?', 'xpath', 'module', 'nodetype'], result['header'])
        self.assertEqual([
            ['+', '/interfaces/interface/config/loopback-mode',
             'openconfig-interfaces', 'leaf'],
            ['+', '/interfaces/interface/state/loopback-mode',
             'openconfig-interfaces', 'leaf'],
            ['+', '/interfaces/interface/state/counters/in-fcs-errors',
             'openconfig-interfaces', 'leaf'],
            ['+', '/interfaces/interface/state/counters/carrier-transitions',
             'openconfig-interfaces', 'leaf'],
            ['-',
             '/interfaces/interface/subinterfaces/subinterface/config/name',
             'openconfig-interfaces', 'leaf'],
            ['+', '/interfaces/interface/subinterfaces/subinterface/state/'
             'counters/in-fcs-errors', 'openconfig-interfaces', 'leaf'],
            ['+', '/interfaces/interface/subinterfaces/subinterface/state/'
             'counters/carrier-transitions', 'openconfig-interfaces', 'leaf'],
        ], result['data'])

    def test_diff_openconfig_interfaces_addons(self):
        fromdata = dataset_for_yangset('test', 'ocif-alpha',
                                       'openconfig-interfaces',
                                       ['min', 'max', 'nodetype'])
        todata = dataset_for_yangset('test', 'ocif-beta',
                                     'openconfig-interfaces',
                                     ['min', 'max', 'nodetype'])
        result = getdiff(fromdata, todata)
        self.assertEqual(['?', 'xpath', 'module', 'min', 'max', 'nodetype'],
                         result['header'])
        self.maxDiff = None
        self.assertEqual([
            ['+', '/interfaces/interface/config/loopback-mode',
             'openconfig-interfaces', '', '', 'leaf'],
            ['+', '/interfaces/interface/state/loopback-mode',
             'openconfig-interfaces', '', '', 'leaf'],
            ['<', '/interfaces/interface/state/last-change',
             'openconfig-interfaces',
             '0', '4294967295', 'leaf'],
            ['>', '/interfaces/interface/state/last-change',
             'openconfig-interfaces',
             '0', '18446744073709551615', 'leaf'],

            ['<', '/interfaces/interface/state/counters/in-unknown-protos',
             'openconfig-interfaces',
             '0', '4294967295', 'leaf'],
            ['>', '/interfaces/interface/state/counters/in-unknown-protos',
             'openconfig-interfaces',
             '0', '18446744073709551615', 'leaf'],

            ['+', '/interfaces/interface/state/counters/in-fcs-errors',
             'openconfig-interfaces',
             '0', '18446744073709551615', 'leaf'],

            ['<', '/interfaces/interface/state/counters/last-clear',
             'openconfig-interfaces', '', '', 'leaf'],
            ['>', '/interfaces/interface/state/counters/last-clear',
             'openconfig-interfaces', '0', '18446744073709551615', 'leaf'],

            ['+', '/interfaces/interface/state/counters/carrier-transitions',
             'openconfig-interfaces',
             '0', '18446744073709551615', 'leaf'],

            ['-',
             '/interfaces/interface/subinterfaces/subinterface/config/name',
             'openconfig-interfaces',
             '', '', 'leaf'],

            ['<', '/interfaces/interface/subinterfaces/subinterface/state/'
             'last-change',
             'openconfig-interfaces',
             '0', '4294967295', 'leaf'],
            ['>', '/interfaces/interface/subinterfaces/subinterface/state/'
             'last-change',
             'openconfig-interfaces',
             '0', '18446744073709551615', 'leaf'],

            ['<', '/interfaces/interface/subinterfaces/subinterface/state/'
             'counters/in-unknown-protos',
             'openconfig-interfaces',
             '0', '4294967295', 'leaf'],
            ['>', '/interfaces/interface/subinterfaces/subinterface/state/'
             'counters/in-unknown-protos',
             'openconfig-interfaces',
             '0', '18446744073709551615', 'leaf'],

            ['+', '/interfaces/interface/subinterfaces/subinterface/state/'
             'counters/in-fcs-errors',
             'openconfig-interfaces',
             '0', '18446744073709551615', 'leaf'],

            ['<', '/interfaces/interface/subinterfaces/subinterface/state/'
             'counters/last-clear',
             'openconfig-interfaces',
             '', '', 'leaf'],
            ['>', '/interfaces/interface/subinterfaces/subinterface/state/'
             'counters/last-clear',
             'openconfig-interfaces',
             '0', '18446744073709551615', 'leaf'],

            ['+', '/interfaces/interface/subinterfaces/subinterface/state/'
             'counters/carrier-transitions',
             'openconfig-interfaces',
             '0', '18446744073709551615', 'leaf']
        ], result['data'])
