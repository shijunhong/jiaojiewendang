#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import random
import requests
import MySQLdb
import MultipartPostHandler
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class V1topicdetailgetTest(MyTest):
    '''主题详情'''
    url_path = '/v1/topic/detail/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_topicdget_success(self):
        '''传必填参数'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id='1081'and is_deleted='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'topicId=' + str(id)
        # params = 'topicId=946'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功',js['message'])

    def test_topicdget_ztsc(self):
        '''传入被删除的主题ID'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id='1081'and is_deleted='1'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'topicId=' + str(id)
        # params = 'topicId=870'
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('获取话题失败',js['message'])

    def test_topicdget_IDlose(self):
        '''主题ID未传，获取失败'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('获取话题失败:话题id是null，请选择一个话题',js['message'])


    def test_topicdget_IDpanull(self):
        '''主题ID的参数为空，获取失败'''
        params = '=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('获取话题失败:话题id是null，请选择一个话题',js['message'])

    def test_topicdget_IDnull(self):
        '''主题ID的值为空，获取失败'''
        params = 'topicId='
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('获取话题失败:话题id是null，请选择一个话题',js['message'])


    def test_topicdget_signerror(self):
        '''sign不正确'''

        params = {'topicId': '1'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params
                        )
        print r




    def test_topicdget_noncerror(self):
        '''nonce不正确'''
        params = {'topicId': '1'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                            params
                        )
        print r

