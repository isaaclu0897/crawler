# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 01:06:50 2017

@author: VX
"""

import os
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import time

#一更，加入時耗、檔案存放位置、檔案分類下載、(下載進度)

start = time.time()

#目標頁面
'''
page_target = str(input('請輸入你想下載的ptt網頁: '))
pos = str(input('請輸入你想要存放的位置: '))
'''
page_target = 'https://www.ptt.cc/bbs/Beauty/index2112.html'
pos = '/home/wei/data/python/photo'
res = requests.get(page_target)
soup = BeautifulSoup(res.text, 'lxml')

#進入到目標頁面中的每個主題頁面
for page in soup.select('.r-ent a'):
    url = 'https://www.ptt.cc' + page['href']
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    del res
    
    #判斷網址中有沒有圖片
    if len(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})) > 0:
        try:
            
            #將路徑cd到欲下載位置，並新增專屬資料夾
            os.chdir(pos)
            os.mkdir('{}'.format(page.text))
            for index, img_url in enumerate(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
                try:
                    #記得更改想要下載到的位置
                    urlretrieve(img_url['href'], '/home/wei/data/python/photo/{}/{}_{}.jpg'.format(page.text ,page.text, index))
                except:
                    print('{} {}_{}.jpg 下載失敗!'.format(img_url['href'], page.text, index))
                finally:
                    del index
        except:
            print('{} can not download {}'.format(page.text, url))
            
    print('{} finish'.format(page.text))
    
print('程式共花費:{:f}秒'.format(time.time() - start))
#https://www.ptt.cc/bbs/Beauty/index2250.html
#E:\\python\\beauty
