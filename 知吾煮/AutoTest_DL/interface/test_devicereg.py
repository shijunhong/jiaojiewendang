#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
import requests
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class deviceregTest(MyTest):
    '''注册饭煲'''
    url_path = '/v1/device/reg'

    @classmethod
    def setUpClass(cls):
        pass

    def test_devicereg_success(self):
        '''注册成功'''
        token = Login().login()  # 引用登录
        params = 'deviceid=81251117&userId=1098742855&ownerId=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], 1)

    def test_devicereg_uslose(self):
        '''测试参数不完整，必填参数(userId)未传'''
        token = Login().login()  # 引用登录
        params = 'deviceid=81251117&ownerId=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('设备使用者为空,禁止注册', js['message'])


    def test_devicereg_delose(self):
        '''测试参数不完整，必填参数(deviceid)未传'''
        params = 'userId=1098742855&ownerId=1098742855&modelName=chunmi.cooker.press1'
        token = Login().login()  # 引用登录
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('设备号为空,禁止注册', js['message'])



    def test_devicereg_owIlose(self):
        '''测试参数不完整，必填参数(ownerId)未传'''
        token = Login().login()  # 引用登录
        params = 'userId=1098742855&deviceid=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('设备拥有者为空,禁止注册', js['message'])

    def test_devicereg_mnlose(self):
        '''测试参数不完整，必填参数(modelName)未传'''
        token = Login().login()  # 引用登录
        params = 'userId=1098742855&deviceid=1098742855&ownerId=1098742855'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('记录设备错误', js['message'])


    def test_devicereg_usnull(self):
        '''必填参数(userId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'userId=&deviceid=1098742855&ownerId=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('设备使用者为空,禁止注册', js['message'])


    def test_devicereg_denull(self):
        '''必填参数(deviceid)的值为空'''
        token = Login().login()  # 引用登录
        params = 'userId=1098742855&deviceid=&ownerId=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('设备号为空,禁止注册', js['message'])



    def test_devicereg_owInull(self):
        '''必填参数(ownerId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'userId=1098742855&deviceid=81251117&ownerId=&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('设备拥有者为空,禁止注册', js['message'])

    def test_devicereg_mnnull(self):
        '''必填参数(modelName)的值为空'''
        token = Login().login()  # 引用登录
        params = 'userId=1098742855&deviceid=81251117&ownerId=1098742855&modelName='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('记录设备错误', js['message'])


    def test_devicereg_uspanull(self):
        '''必填参数(userId)为空'''
        token = Login().login()  # 引用登录
        params = '=1098742855&deviceid=81251117&ownerId=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('设备使用者为空,禁止注册', js['message'])


    def test_devicereg_depanull(self):
        '''必填参数(deviceid)为空'''
        token = Login().login()  # 引用登录
        params = 'userId=1098742855&=81251117&ownerId=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('设备号为空,禁止注册', js['message'])



    def test_devicereg_owIpanull(self):
        '''必填参数(ownerId)为空'''
        token = Login().login()  # 引用登录
        params = 'userId=1098742855&deviceid=81251117&=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('设备拥有者为空,禁止注册', js['message'])

    def test_devicereg_mnpanull(self):
        '''必填参数(modelName)为空'''
        token = Login().login()  # 引用登录
        params = 'userId=1098742855&deviceid=81251117&ownerId=1098742855&=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('记录设备错误', js['message'])

    def test_devicereg_tokenull(self):
        '''未传入token'''
        params = 'userId=1098742855&deviceid=81251117&ownerId=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_devicereg_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        params = 'userId=1098742855&deviceid=81251117&ownerId=1098742855&modelName=chunmi.cooker.press1'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token+'eee'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_devicereg_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'deviceid': '160812',
                                   'mac': '1608121',
                                   'userId': '1608122',
                                   'online': '1',
                                   'cityName': '120100',
                                   'ownerId': '160812',
                                   'ownerName': '1608124',
                                   'modelName': '1608125'
                                   }
        print params
        r = self.signerror('POST',
                        self.url_path,
                        params,
                        self.token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'deviceid': '160812',
        #                            'mac': '1608121',
        #                            'userId': '1608122',
        #                            'online': '1',
        #                            'cityName': '120100',
        #                            'ownerId': '160812',
        #                            'ownerName': '1608124',
        #                            'modelName': '1608125'
        #                            })
        # print u"传入的参数为：" + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + '1')
        # request.add_header('token', self.token )
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_devicereg_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'deviceid': '160812',
                  'mac': '1608121',
                  'userId': '1608122',
                  'online': '1',
                  'cityName': '120100',
                  'ownerId': '160812',
                  'ownerName': '1608124',
                  'modelName': '1608125'
                  }

        print params
        r = self.noncerror('POST',
                           self.url_path,
                           params,
                           self.token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'deviceid': '160812',
        #                            'mac': '1608121',
        #                            'userId': '1608122',
        #                            'online': '1',
        #                            'cityName': '120100',
        #                            'ownerId': '160812',
        #                            'ownerName': '1608124',
        #                            'modelName': '1608125'
        #                            })
        # print u"传入的参数为：" + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce + '1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature )
        # request.add_header('token', self.token )
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
        #



if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(deviceregTest('test_devicereg_success'))
    testunit.addTest(deviceregTest('test_devicereg_delose'))
    testunit.addTest(deviceregTest('test_devicereg_uslose'))
    testunit.addTest(deviceregTest('test_devicereg_owIlose'))
    testunit.addTest(deviceregTest('test_devicereg_mnlose'))
    testunit.addTest(deviceregTest('test_devicereg_denull'))
    testunit.addTest(deviceregTest('test_devicereg_usnull'))
    testunit.addTest(deviceregTest('test_devicereg_owInull'))
    testunit.addTest(deviceregTest('test_devicereg_mnnull'))
    testunit.addTest(deviceregTest('test_devicereg_depanull'))
    testunit.addTest(deviceregTest('test_devicereg_uspanull'))
    testunit.addTest(deviceregTest('test_devicereg_owIpanull'))
    testunit.addTest(deviceregTest('test_devicereg_mnpanull'))
    testunit.addTest(deviceregTest('test_devicereg_tokenerror'))
    testunit.addTest(deviceregTest('test_devicereg_tokenull'))
    testunit.addTest(deviceregTest('test_devicereg_signerror'))
    testunit.addTest(deviceregTest('test_devicereg_noncerror'))


    fp = open('./devicereg_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'注册饭煲接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()













