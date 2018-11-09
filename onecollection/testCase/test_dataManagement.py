#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaoqing

import unittest
import os
import requests
import json
import time

class DataManagermentTest(unittest.TestCase):
    def setUp(self):
        self.r = requests.post(url='http://collection.admin.test.com/onecollection_admin/login',
                                json={"account": "13344447777", "passwd": "123456"},
                                headers={"Content-Type": "application/json;charset=UTF-8"})
        self.cookies = json.loads(self.r.text)['data']['session_key']


    def tearDown(self):
        pass


    def get_hearder(self):
        """对请求头做数据分离"""
        self.header = {"Content-Type":"application/json;charset=UTF-8"}
        return self.header



    def test_001(self):
        """数据监测-图表监测:返回的批次"""
        # with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'Interface','cookies'),'r') as f:
        #     cookie = f.read()
        r = requests.get(url='http://collection.admin.test.com/onecollection_admin/dataAnalyze/query_batchno_and_batchremark',
                         headers=self.get_hearder(),
                         cookies={'admin_session_key':self.cookies})
        """对返回结果反序列化"""
        dict1 = json.loads(r.text)
        """对响应结果断言"""
        self.assertEqual(dict1['code'],0)


    def test_002(self):
        """数据监测-图标监测:返回的城市"""
        r = requests.post(url='http://collection.admin.test.com/onecollection_admin/dataAnalyze/query_monitor_city',
                          headers=self.get_hearder(),
                          cookies={'admin_session_key':self.cookies},
                          json={"time":"近30天",
                                "city_id":"",
                                "city_name":"",
                                "batch_no":"20180929155302",
                                "column_type":"",
                                "arrears_age":"",
                                "begin_time":1539170797055,
                                "end_time":1541676397055,
                                "query_type":""})
        dict2 = json.loads(r.text)
        """对响应结果断言"""
        self.assertEqual(dict2['code'],0)

    def test_003(self):
        """数据监测-图标监测:4个图表"""
        r = requests.post(url='http://collection.admin.test.com/onecollection_admin/dataAnalyze/query_debtor_monitor_charts_stat',
                          headers=self.get_hearder(),
                          cookies={'admin_session_key': self.cookies},
                          json={"time": "近30天",
                                "city_id": "370600",
                                "city_name": "烟台市",
                                "batch_no": "20180929155302",
                                "column_type": "totalRepayUser",
                                "arrears_age": "4",
                                "begin_time": 1539170797055,
                                "end_time": 1541676397055,
                                "query_type": ""})
        dict3 = json.loads(r.text)
        """对响应结果断言"""
        self.assertEqual(dict3['code'], 0)
        """对返回城市断言"""
        self.assertEqual(str(dict3['data']['city']['legend']['data'][0]),'烟台市')


#如何使用数据库查询出来的数据与接口返回数据进行断言
#如何用jenkins自动构建任务
#如何用git上传并保存代码

#对数据封装的理解
#进行有效的数据分离
#使用excel文件保管测试用例

#重看无涯接口自动化测试，整理其代码


if __name__ == '__main__':
    unittest.main(verbosity=2)
