# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 19:11:22 2017

@author: VX
"""

import requests
import time
import bs4

start = time.time()


url = 'https://www.ptt.cc/bbs/Beauty/index2181.html'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'lxml')
rent = soup.select('.r-ent')
for i in rent:
    print('推文: %s' %(i.select('.nrec')[0].text))
#   print(i.select('.mark'))
    print('標題: %s'%(i.select('.title')))
#   print(i.select('.meta'))
    print('日期: %s' %(i.select('.date')[0].text))
    print('作者: %s' %(i.select('.author')[0].text))



print ()
print ('程式花費時間共計: %f秒' %(time.time() - start))

