# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 17:47:38 2017

@author: Wei
"""

import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re

# 原始代碼

# 目標頁面
page_target = 'https://www.ptt.cc/bbs/Beauty/index2250.html'
res = requests.get(page_target)
soup = BeautifulSoup(res.text, 'lxml')

# 進入到目標頁面中的每個主題頁面
for page in soup.select('.r-ent a'):
    print(page['href'])
    url = 'https://www.ptt.cc' + page['href']
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    del res
    
    # 判斷網址中有沒有圖片
    if len(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})) > 0:
        for index, img_url in enumerate(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
            try:
                
                # 記得更改想要下載到的位置
                urlretrieve(img_url['href'], 'E:\\python\\beauty\\{}_{}.jpg'.format(page.text, index))
            except:
                print('{} {}_{}.jpg 下載失敗!'.format(img_url['href'], page.text, index))
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
