#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class recipeinfootherTest(MyTest):
    '''获取食谱其他相关信息'''
    url_path =  '/v1/recipe/info/other/1733'

    @classmethod
    def setUpClass(cls):
        pass


    def test_recipeinfo_success(self):
        '''获取食谱其他相关信息'''
        token = Login().login()  # 引用登录
        r = self.bujiami('GET',
                         self.url_path,
                         { '': ''},
                         token
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取食谱其他相关信息成功', js['message'])

    def test_recipeinfo_success1(self):
        '''获取食谱其他相关信息'''
        r = self.bujiami('GET',
                         self.url_path,
                         { '': ''}

                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取食谱其他相关信息成功', js['message'])



    def test_recipeinfo_signerror(self):
        '''sign不正确'''
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "GET", self.url)
        request = urllib2.Request(self.url )
        request.add_header('nonce',self.nonce)
        request.add_header('User-Agent','chunmiapp')
        request.add_header('signature',self.signature+'1')
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


    def test_recipeinfo_noncerro(self):
        '''nonce不正确'''
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "GET", self.url)
        request = urllib2.Request(self.url )
        request.add_header('nonce',self.nonce+'1')
        request.add_header('User-Agent','chunmiapp')
        request.add_header('signature',self.signature)
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])




if __name__ == '__main__':
    # unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(recipeinfoTest('test_recipeinfo_success'))
    testunit.addTest(recipeinfoTest('test_recipeinfo_signerror'))
    testunit.addTest(recipeinfoTest('test_recipeinfo_noncerro'))



    fp = open('./recipeinfo.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'获取食谱详情信息接口测试报告',
                            description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()
