# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/28 9:59
@Author  : ZZINDS
@Site    : 
@File    : proxy.py
@Software: N M $ L ®
"""
import urllib.request
import urllib
import re
import time
import socket
import threading
import telnetlib

# 整理代理IP格式
proxys = []
inFile = open('proxy.txt', 'r')
proxy_ip = open('proxy_ip.txt', 'w')  # 新建一个储存有效IP的文档

for line in inFile.readlines():
    line = line.strip('\n')
    #proxy_host = '://'.join(line.split('='))
    proxy_host = line.split('=')[0]
    # print(proxy_host)
    proxy_temp = {line.split("=")[0]: proxy_host}
    print(proxy_temp)
    proxys.append(proxy_temp)

lock = threading.Lock()  # 建立一个锁


# 验证代理IP有效性的方法
def test(i):
    socket.setdefaulttimeout(5)  # 设置全局超时时间
    # url = "http://quote.stockstar.com/stock"  #打算爬取的网址
    url = "http://www.baidu.com/"  # 打算爬取的网址
    try:
        proxy_support = urllib.request.ProxyHandler(proxys[i])
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)")]
        urllib.request.install_opener(opener)
        res = urllib.request.urlopen(url).read()

        # 获取锁，用于线程同步
        lock.acquire()  # 获得锁
        print(proxys[i], 'is OK')
        proxy_ip.write('%s\n' % str(proxys[i]))  # 写入该代理IP

        # 释放锁，开启下一个线程
        lock.release()  # 释放锁
    except Exception as e:
        lock.acquire()
        print(proxys[i], e)
        lock.release()
    # 单线程验证


'''''for i in range(len(proxys)): 
    test(i)'''
# 多线程验证
threads = []
start = time.clock()
for i in range(len(proxys)):
    thread = threading.Thread(target=test, args=[i])
    threads.append(thread)
    thread.start()
# 阻塞主进程，等待所有子线程结束
for thread in threads:
    thread.join()

proxy_ip.close()  # 关闭文件

end = time.clock()
print("开始时间: %f s" % start)
print("结束时间: %f s" % end)
print("校验IP耗时: %f s" % (end - start))

try:
    telnetlib.Telnet('47.105.149.199', port='80', timeout=5)
except:
    print('链接失败')
else:
    print('链接成功')