# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:12:34 2017

@author: VX
"""

import requests
import time
from bs4 import BeautifulSoup as bf

start = time.time()


url = 'https://www.ptt.cc/bbs/Beauty/index2181.html'
res = requests.get(url)
soup = bf(res.text,'lxml')
rent = soup.select('.r-ent')

print (' 日期     作者                 推文   標題')
for i in rent:
    print('%-9s %-20s %-5s %-100s 網址 : %s' %((i.select('.date')[0].text),
                                               (i.select('.author')[0].text),
                                               (i.select('.nrec')[0].text),
                                               (i.select('.title a')[0].text),
                                               (i.select('.title a')[0])))
    print ()

#   print(i.select('.mark'))
#   print(i.select('.meta'))

for article in soup.select('.r-ent a'):
    url = 'https://www.ptt.cc' + article['href']
    print (url)

print ()
print ('程式花費時間共計: %f秒' %(time.time() - start))