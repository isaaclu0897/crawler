#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 18:01:47 2017

@author: VX
"""
import os
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import time

#二更，目標頁面爬取更新，新增連續下載，人性化輸入

start = time.time()

# 目標頁面 
page_target = 'https://www.ptt.cc/bbs/Beauty/index1231.html'
dwn_page_num = 500
path = '/home/wei/ptt/beauty'
push = 60
count = 1
add = 0

# 跳轉到下一個目標頁面
while count<=dwn_page_num:
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
    for page in soup.select('.r-ent'):
        name = page.select('a')[0].text
        page_index = page.select('.title a')[0]['href']
        article_push = page.select('.nrec')[0].text
        
        # 解析文章推文數
        if article_push.isdigit():
            article_push = int(article_push)
        elif article_push == '爆':
            article_push = 99
        else:
            article_push = 0
            
        # 過設定推文數方下載
        if article_push >= push:
            url = 'https://www.ptt.cc' + page_index
            print('推：{}, 標題：{}, 網址：{}'.format(article_push, name, url))
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'lxml')
            del res
            
            pattern = re.compile(r'https?://i?.?imgur.com/.*')
            img_url = soup.findAll('a', {'href':(pattern)})
            
            # 判斷網址中有沒有圖片
            if len(img_url) > 0:
                try:
    
                    # 將路徑cd到欲下載位置，並新增專屬資料夾
                    if not os.path.isdir(path):
                        os.mkdir(path)
                    else:
                        os.chdir(path)
                    if not os.path.isdir(name):
                        os.mkdir('{}'.format(name))
                    for index, img_url in enumerate(img_url):
                        try:
                            urlretrieve(img_url['href'], path + '/{}/{}_{}.jpg'.format(name ,name, index))
                        except:
                            print('{} {}_{}.jpg 下載失敗!'.format(img_url['href'], name, index))
                        finally:
                            del index
                    print('{} finish'.format(name))
                except:
                    print('{} can not download url:{}'.format(name, url))
                    
print('程式共花費:{:f}秒'.format(time.time() - start))         
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
