#coding=utf-8
from CJcryp import *
import json
import requests
import unittest
import time
import urllib, urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class CJMyTest(unittest.TestCase):

    def setUp(self):
        # self.base_url = 'https://testapi2.coo-k.com'
        self.base_url = 'http://10.0.10.100:17001'
        # self.base_url = 'https://twcnpotplug.joyami.com'
        # self.base_url = 'https://framipotplugapi.joyami.com'
        self.nonce = generateNonce()
        self.key = getSessionSecurity(self.nonce)

    def cjmyhttp(self,method, url_path=None,post_data=None,token=None):
        url = self.base_url + url_path
        self.signature = generateSignature(self.nonce,method, url)
        params = urllib.urlencode(post_data)
        encoded = encryptAES(params, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': self.signature,
                   'token': token
                   }
        if method == 'GET':
            url2 = url + '?' + payload
            request = urllib2.Request(url2, headers=headers)
            # response = urllib2.urlopen(request)
            # result = response.read()
            # s = decryptAES(result, self.key)
            # return s
        if method == 'POST':
            request = urllib2.Request(url, data=payload, headers=headers)
            # response = urllib2.urlopen(request)
            # result = response.read()
            # s = decryptAES(result, self.key)
            # return s
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        s = decryptAES(result, self.key)
        return s

    def cjbujiami(self,method, url_path=None,post_data=None,token=None):
        url = self.base_url + url_path
        self.signature = generateSignature(self.nonce,method, url)
        params = urllib.urlencode(post_data)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': self.signature,
                   'token': token
                   }
        if method == 'GET':
            url2 = url + '?' + params
            request = urllib2.Request(url2, headers=headers)
        if method == 'POST':
            request = urllib2.Request(url, data=params, headers=headers)
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        return result
        # s = decryptAES(result, self.key)
        # return s

    def tearDown(self):
        pass