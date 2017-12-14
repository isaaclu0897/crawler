# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 15:03:47 2017

@author: VX
"""

import requests
import bs4

url = 'http://www.xinshipu.com/zuofa/49391'
head = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

res = requests.get(url, headers = head)
soup = bs4.BeautifulSoup(res.text, 'lxml')
reup = soup.select('.re-up')[0]