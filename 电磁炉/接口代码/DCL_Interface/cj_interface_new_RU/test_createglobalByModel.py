#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 15:38
# @Author  : fengguifang
# @File    : test_createglobalByModel.py
# @Software: PyCharm
from base.base import MyTest
import json
import requests
requests.packages.urllib3.disable_warnings()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class createglobalByModelTest(MyTest):
    '''根据model创建一个自定义模式'''
    url_path = '/v1/recipe/collect/createglobalByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_createglobalByModel_success(self):
        '''所有必填字段都传'''
        payload ={'name':'mmda1','firePower':26,'duration':60,'temperature':0,'model':self.model,'language': self.language}
        r = self.cry_myhttp('POST',
                         self.url_path,
                        json.dumps(payload),
                         )
        print r
        js = json.loads(r)
        print js['result']['recipe']['id']
        self.assertEqual(js['code'], 1)
        self.assertEqual(js['message'], 'success')


