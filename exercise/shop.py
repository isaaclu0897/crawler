# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 01:09:24 2018

@author: VX
"""
import requests
from bs4 import BeautifulSoup as bf

url = 'http://www.coolpc.com.tw/evaluate.php'
res = requests.get(url)
soup = bf(res.text, 'lxml')
print(soup)
print(soup.prettify())
soup = soup.select('center tbody')[0]
s = soup.select('tr[bgcolor="efefe0"]')[6]
a = s.select('optgroup')[0]'''
#print(a)
'''
for i in a.select('option'):
    print(i.text, end='')'''