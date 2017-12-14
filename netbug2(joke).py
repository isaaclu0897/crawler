# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:19:20 2017

@author: VX
"""
import requests
import time
import bs4

start = time.time()
url = 'https://www.ptt.cc/bbs/joke/index.html'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'lxml')

for i in soup.select('.r-ent'):

    print (i.select('.title')[0].text)
    print (i.select('.date')[0].text)
    print (i.select('.author')[0].text)

print ()
print ('程式花費時間共計: %f秒' %(time.time() - start))