# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/27 15:27
@Author  : ZZINDS
@Site    : 
@File    : demo.py
@Software: N M $ L ®
"""
#使用requests

#import requests

#try:
#    requests.get('http://www.baidu.com/', proxies={"http":"http://117.127.0.196:80"})
#except:
#    print('链接失败')
#else:
#    print('链接成功')

#使用telnet


import telnetlib

try:
    telnetlib.Telnet('183.151.42.23', port='8070', timeout=5)
except:
    print('链接失败')
else:
    print('链接成功')


