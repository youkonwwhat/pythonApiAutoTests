#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaoqing

import HTMLTestRunner
import unittest
import os

def all_testCase():
    """返回所有的测试用例"""
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),'testCase'),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

def run():
    """生成测试报告"""
    fp = open('testReport.html','wb')
    HTMLTestRunner.HTMLTestRunner(stream=fp,
                                  title='客户监测接口自动化测试报告',
                                  description='基于python').run(all_testCase())


run()