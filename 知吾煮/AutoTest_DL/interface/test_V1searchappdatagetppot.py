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

class V1searchappdatagetTest(MyTest):
    '''搜索接口(能搜索到电磁炉食谱)'''
    # url_path = '/v1/community/search/app/data/getnew'
    # '&deviceModel=chunmi.cooker.press1'
    url_path = '/v1/community/search/app/data/getpotandinduction'

    @classmethod
    def setUpClass(cls):
        pass

    def test_searchappdataget_success134(self):
        '''传入所有参数'''
        self.base_url = 'https://cinapi.joyami.com'
        url = self.base_url + self.url_path
        print url
        signature = generateSignature(self.nonce,  'GET', url)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': signature
                   }
        # params = {'param': 'value', 'param': 'value'}
        # payload1 = urllib.urlencode(params)
        params = 'content=排骨汤&pageno=1&perpage=200'
        encoded = encryptAES(params, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        r = requests.get(url, params=payload, headers=headers, verify=False)
        result = r.text.encode()
        print result
        s = decryptAES(result, self.key)
        print s
        js = json.loads(s)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name']
            print js['result'][i]['id']


        #     # json_response = json.loads(s)
        #     return s
        # except Exception as e:
        #     print('%s' % e)
        #     return {}
        #
        # params = 'content=鸡蛋&pageno=1&perpage=200'
        # # params = {'content':'油',
        # #          'pageno':'1',
        # #           'perpage':'10'}
        # r = self.myhttp('GET',
        #                 self.url_path,
        #                  params
        #                  )
        # print r
        # js = json.loads(r)
        # self.assertEqual(js['state'], 1)
        # for i in range(len(js['result'])):
        #     print js['result'][i]['name']



    def test_searchappdataget_success(self):
        '''传入所有参数'''
        params = 'content=鸡蛋&pageno=1&perpage=200'
        # params = {'content':'油',
        #          'pageno':'1',
        #           'perpage':'10'}
        r = self.myhttp('GET',
                        self.url_path,
                         params
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name']

    def test_searchappdataget_success1(self):
        '''传入所有参数'''
        params = 'content=土豆&pageno=1&perpage=200&dmgs=1'
        # params = {'content':'油',
        #          'pageno':'1',
        #           'perpage':'10'}
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name']

    def test_searchappdataget_success2(self):
        '''传入所有参数'''
        params = 'content=土豆&pageno=1&perpage=200&dmgs2=1'
        # params = {'content':'油',
        #          'pageno':'1',
        #           'perpage':'10'}
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name']

    def test_searchappdataget_btsuccess(self):
        '''传入必填参数'''
        params = 'pageno=1&perpage=20'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_searchappdataget_nolose(self):
        '''必填参数pageno未传，默认显示第1页的数据'''
        params = 'perpage=20'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_searchappdataget_nonull(self):
        '''必填参数pageno的值为空，默认显示第1页的数据'''
        params = 'pageno=&perpage=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_searchappdataget_nopanull(self):
        '''必填参数pageno的参数为空，默认显示第1页的数据'''
        params = '=1&perpage=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_searchappdataget_gelose(self):
        '''必填参数perpage未传'''
        params = 'pageno=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 2)


    def test_searchappdataget_genull(self):
        '''必填参数perpage的值为空'''
        params = 'pageno=1&perpage='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 2)

    def test_searchappdataget_gepanull(self):
        '''必填参数perpage的参数为空'''
        params = 'pageno=1&=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 2)



    def test_searchappdataget_signerror(self):
        '''sign不正确'''
        params = {'pageno': '1','perpage':'5'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = 'pageno=1&perpage=5'
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + 'e'
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])

    def test_searchappdataget_noncerror(self):
        '''nonce不正确'''
        params = {'pageno': '1','perpage':'5'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])

        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = 'pageno=1&perpage=5'
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce + 'e',
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


