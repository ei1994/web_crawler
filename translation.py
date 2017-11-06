# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:36:16 2017

@author: Administrator
"""

import urllib.request
import urllib.error

'''
用于访问百度的自动翻译
'''
import urllib.request
import urllib.parse
import json
import time
import random
#下载图片
def download():

    response=urllib.request.urlopen('http://sv14.haoi23.net:8009/pic/21/1004_14_21213213BE9FA2LL6H.gif')
    time.sleep(10)
    cat_img=response.read()

    with open('cat1.jpg','wb') as f:
        f.write(cat_img)

#翻译
def translate():
    while True:

        url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        data={}
        head={}
        data['from']='AUTO'
        data['to']='    AUTO'
        data['smartresult']='   dict'
        data['client']='fanyideskweb'
        data['salt']='1505997607810'
        data['sign']='dd12b4d2fc81d98f09dd660702e027ae'
        data['doctype']='   json'
        data['version']='   2.1'
        data['keyfrom']='   fanyi.web'
        data['action']='    FY_BY_REALTIME'
        data['typoResult']='true'
        head['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'
        data['i']='天天向上'

        data=urllib.parse.urlencode(data).encode('utf-8')
        req=urllib.request.Request(url,data,head)
        response=urllib.request.urlopen(url,data)
        html=response.read().decode('utf-8')

        target=json.loads(html)  # str转成dict
        print(target,'\n\n\n',req.headers)

        time.sleep(5)

#代理
def proxy():

    url= 'http://www.whatismyip.com.tw'
    iplist=['122.72.32.74   :80','122.72.32.88:80','183.159.2.87:80']
    proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)}) #1

    opener=urllib.request.build_opener(proxy_support)#2

    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]
    urllib.request.install_opener(opener) #3

    response=urllib.request.urlopen(url)

    html=response.read().decode('utf-8')

    return html

html=translate()
with open('test','w') as f:
    f.write(html)
print(html)
