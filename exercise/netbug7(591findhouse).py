# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:39:13 2017

@author: VX
"""

import requests
import bs4
import time

start = time.time()

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
res = requests.get('https://buy.yungching.com.tw/region?pg=2', headers = head)
print (res.text)

print ('程式共花費: %f秒' %(time.time() - start))

