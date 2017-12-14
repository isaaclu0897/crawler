# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 14:03:24 2017

@author: VX
"""
import requests
import time

start = time.time()
url = 'https://www.ptt.cc/bbs/joke/index.html'
res = requests.get(url)

print (res.text)

print ('程式花費時間共計: %f' %(time.time() - start))
