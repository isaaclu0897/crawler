# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:12:13 2017

@author: VX
"""

import requests
import bs4
import time

start = time.time()


payload ={
        'from':'/bbs/gossiping/index.html',
        'yes':'yes'
        }

rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18',data=payload)

res = rs.get('https://www.ptt.cc/bbs/gossiping/index.html')
soup = bs4.BeautifulSoup(res.text,'lxml')
'''
res = requests.get('https://www.ptt.cc/bbs/gossiping/index.html')
print (res.text)
'''
'''
gossiping版不能直接用beauty版打法，會出現post問題
'''

rent = soup.select('.r-ent')
for i in rent:
    print ((i.select('.nrec')[0].text))
#    print (i.select('.mark'))
    print ('日期  :%s' %(i.select('.date')[0].text))
#    print (i.select('.meta'))
    print ('作者  : %s' %(i.select('.author')[0].text))
    print ('標題  :%s' %(i.select('.title a')))
    print ()

print ('程式共花費: %f秒' %(time.time() - start))
