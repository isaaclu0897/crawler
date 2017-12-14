# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:37:44 2017

@author: VX
"""

import requests
import bs4
import shutil
import time

start = time.time()

res = requests.get('http://www.gamebase.com.tw/forum/64172/topic/96278769/1')
soup = bs4.BeautifulSoup(res.text,'lxml')

for i in soup.select('.img'):
   
   # print (i['src'], i['src'].split('/')[-1])
   
   filename = i['src'].split('/')[-1]
   res2 = requests.get(i['src'], stream = True)
   f = open (filename, 'wb')
   shutil.copyfileobj(res2.raw, f)
   f.close()
   del res2

print ('程式共花費: %f秒' %(time.time() - start))
