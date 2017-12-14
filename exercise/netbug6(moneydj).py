# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 21:47:33 2017

@author: VX
"""

import requests
import bs4
import time

start = time.time()

res = requests.get('https://www.moneydj.com/KMDJ/News/NewsViewer.aspx?a=a180a15b-9e4f-4575-b28f-927fcb5c63a3')
soup = bs4.BeautifulSoup(res.text,'lxml')
'''print (soup.select('.contentMasterTable'))'''

for i in soup.select('.contentMasterTable'):
    print (i.select('.viewer_tl')[0].text)
    print (i.select('.float_right'))



print ('程式共花費: %f秒' %(time.time() - start))


'''
id # class . 

'''