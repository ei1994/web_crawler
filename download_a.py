# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:32:29 2017

@author: Administrator
"""

import requests
import re
import os
import time

headers = {
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "en-US,zh-CN;q=0.8,zh;q=0.6,en;q=0.4",
           "Cache-Control": "no-cache",
           "Connection": "keep-alive",
#           "Cookie":"__cfduid=dd46a11309e3cb65a78d0caa56ed4daa51505911332;UM_distinctid=15ea106f08fe9-0ff84cf70e488a8-75246751-1fa400-15ea106f090c7; CNZZDATA5003870=cnzz_eid%3D1164409310-1505910966-null%26ntime%3D1506062459; Hm_lvt_93e96130e9baaf094d30957b36d95ccf=1505940143,1506081081; pgv_pvi=2985106432; _qddaz=QD.92erq0.v00p7w.j7thvo7t; tencentSig=5302248448;user=uid=623345387&pwd=a12345678; ASP.NET_SessionId=vvvcypp2d2o4cbnhn4bngu5b; IESESSION=alive; _qddab=3-z416qh.j7w1gs75; Hm_lpvt_93e96130e9baaf094d30957b36d95ccf=1506081081; pgv_si=s5910183936; _qdda=3-1.2x97cs; _qddamta_800058301=3-0",
           "Cookie":"__cfduid=d1cd5a3a0802ebb9cab7d2973f44bc5ca1505830099; UM_distinctid=15e9a791386a9-05d459887c7e78-36465d60-100200-15e9a79138762; pgv_pvi=7775123456; __guid=166899000.1935821023027210800.1505907169248.0813; yjs_id=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTUuMC4yODgzLjg3IFNhZmFyaS81MzcuMzZ8d3d3Lmhhb2kyMy5uZXR8MTUwNTkwNzE2OTczMnxodHRwOi8vd3d3Lmhhb2kyMy5uZXQvP3B0PXQ; tencentSig=8586044416; ASP.NET_SessionId=4w5cxxby0kzbrnbgv0t4caxq; IESESSION=alive; Hm_lvt_93e96130e9baaf094d30957b36d95ccf=1505872238,1505958438,1506041710,1506310782; Hm_lpvt_93e96130e9baaf094d30957b36d95ccf=1506310782; ctrl_time=1; pgv_si=s3970691072; user=uid=623345387&pwd=a12345678; monitor_count=7; CNZZDATA5003870=cnzz_eid%3D46441260-1505905552-%26ntime%3D1506322448; AJSTAT_ok_pages=1; AJSTAT_ok_times=11; _qddaz=QD.76tm55.fahzfd.j7roes3f; _qddamta_800058301=3-0; _qdda=3-1.2x97cs; _qddab=3-odccan.j7zuy9ei",
           "Pragma": "no-cache",
           "Referer": "http://www.haoi23.net/login.aspx?act=reg",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
         }

def dowmloadPic(html, page):
    i = 0
    print ('找到第'+str(page)+'页的图片，现在开始下载图片...')
#    src = html
    links_names= re.findall(r"<img src='(.*?)'.+?<td>(\w{4,5})</td>", html, re.S)
#    print(links)
    for each, name in links_names:
        if each==None:
            continue
        if re.search(r'\d{4}',name):
            if len(name)==4:
                print( '正在下载第'+str(i+1)+'张图片，图片名称:'+name+'，图片地址：'+str(each))
                try:
                    pic= requests.get(each, timeout=10)
                except requests.exceptions.ConnectionError:
                    print ('【错误】当前图片无法下载')
                    continue
                time.sleep(1)
                string = 'pictures/'+ str(page) +'_' + str(name)+'.jpg'
                with open(string,'wb') as fp:
                    fp.write(pic.content)
        i += 1

if __name__ == '__main__':
    
    session=requests.Session()
    
    if os.path.exists('pictures') is False:
        os.makedirs('pictures')
        
    start = input("Input start page: ")
    end = input("Input last page: ")
    while(int(end)<int(start)):
        print('Last must be > start! Please input again.')
        end = input("Input last page: ")

    base_url = 'http://www.haoi23.net/u_3mypic.aspx?day=all&s=0&e=23&page={pageNum}'
    for i in range(int(start), int(end)+1):
        url = base_url.format(pageNum=i)
        result = session.get(url, headers=headers)
        #print(result.text)
        dowmloadPic(result.text, i)
    


