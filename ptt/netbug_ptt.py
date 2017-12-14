# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:43:49 2017

@author: Wei
"""

import os
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import time

#二更，目標頁面爬取更新，新增連續下載，交互式輸入

start = time.time()

# 目標頁面
'''
page_target = str(input('請輸入你想下載的ptt網頁\nex:https://www.ptt.cc/bbs/Beauty/index2101.html\n>>>'))
page_number = int(input('請輸入想要下載的頁數\nex:2\n>>>'))
path = str(input('請輸入你想要存放的位置\nex:C:\\Users\\VX\\Downloads\\123123\n>>>'))
'''
page_target = 'https://www.ptt.cc/bbs/Beauty/index2101.html'
page_number = 5
path = '/home/wei/data/python/photo'

count = 0
add = 0
# 跳轉到下一個目標頁面
while count<=page_number:
    chnum = str(int(''.join([x for x in page_target if x.isdigit()])) + add) # 抽取 url index置換成下個頁面的 index
    page_target = page_target.split('/')
    page_target[-1] = ('index{}.html'.format(chnum))
    page_target = '/'.join(page_target)
    print(page_target)
    add = 1
    count += 1

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
                if not os.path.isdir(path):
                    os.mkdir(path)
                os.chdir(path)
                if not os.path.isdir(page.text):
                    os.mkdir('{}'.format(page.text))
                for index, img_url in enumerate(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
                    try:
                        urlretrieve(img_url['href'], path + '/{}/{}_{}.jpg'.format(page.text ,page.text, index))
                    except:
                        print('{} {}_{}.jpg 下載失敗!'.format(img_url['href'], page.text, index))
                    finally:
                        del index
            except:
                print('{} can not download {}'.format(page.text, url))
                                    
        print('{} finish'.format(page.text))
        
                                    
print('程式共花費:{:f}秒'.format(time.time() - start))

