# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:00:23 2017

@author: VX
"""

import requests
import bs4
import time

start = time.time()


payload ={
        'from':'/bbs/Gossiping/index.html',
        'yes':'yes'
        }

rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18',data=payload)

res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html')
#print (res.text)
soup = bs4.BeautifulSoup(res.text,'lxml')
a = soup.find('a')
#print (soup)
print ('------------------------------------------------------------------------')
print (soup.find('div'))
print ('------------------------------------------------------------------------')
print (soup.find('div','r-ent'))
print ('------------------------------------------------------------------------')
print (soup.find('div','r-ent','nrec','h1 f2'))
print ('1------------------------------------------------------------------------')
print (soup.find('div','nrec'))
print ('------------------------------------------------------------------------')
print (soup.find('div','title','a'))
print ('------------------------------------------------------------------------')
print (soup.find('a',href='/bbs/Gossiping/M.1496655879.A.753.html'))
print ('3------------------------------------------------------------------------')
print(a['href'], a.text)
print ()
print(soup.find('h1'))
'''
rent = soup.find_all('div','r-ent')
for i in rent:
    print (i.find('nrec'))
'''
print ('程式共花費: %f秒' %(time.time() - start))