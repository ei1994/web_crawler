# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:36:27 2017

@author: Administrator
"""
import re
import requests
import os

def dowmloadPic(html,keyword):

    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    print ('找到关键词:'+keyword+'的图片，现在开始下载图片...')
    for each in pic_url:
        print ('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
        try:
            pic= requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print ('【错误】当前图片无法下载')
            continue
        string = 'pictures\\'+keyword+'_'+str(i) + '.jpg'
        with open(string,'wb') as fp:
            fp.write(pic.content)
        i += 1

if __name__ == '__main__':
    
    session = requests.Session()
    if os.path.exists('pictures') is False:
        os.makedirs('pictures')
    word = input("Input key word: ")
#    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=' +word 
    result = session.get(url)
    dowmloadPic(result.text,word)
