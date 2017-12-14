# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:49:42 2017

@author: VX
"""

import requests
from bs4 import BeautifulSoup as bf
import re

url = 'https://www.ptt.cc/bbs/Beauty/M.1496667743.A.2B1.html'
res = requests.get(url)
soup = bf(res.text, 'lxml')


for i in soup:
    print(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')}))


