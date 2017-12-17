#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 00:14:26 2017

@author: wei
"""
from urllib.request import urlretrieve
import re
import time
from nbtool import change_page, parse_url, mk_exclusivedir, ptt, PTT_atc

#三更，可按讚數下載, 及模組化

start = time.time()

# 目標頁面
'''
page_target = str(input('請輸入你想下載的ptt網頁\nex:https://www.ptt.cc/bbs/Beauty/index2102.html\n>>>'))
page_number = int(input('請輸入想要下載的頁數\nex:20\n>>>'))
path = str(input('請輸入你想要存放的位置\nex:/home/wei/data/python/ptt_photo\n>>>'))
'''
page_target = 'https://www.ptt.cc/bbs/Beauty/index2102.html'
page_number = 2
path = '/home/wei/data/python/ptt_photo'

count = 0
page_target = change_page.page(page_target, -1, printu=False)     # 換頁
# 跳轉到下一個頁面
while count<=page_number:
    page_target = change_page.page(page_target)
    count += 1
    msoup = parse_url(page_target)                  # 頁面解析
    # 進入到目標頁面中的每個主題頁面
    for page in msoup.select('.r-ent'):
        Pnum = PTT_atc.push_num(page)
        url = PTT_atc.url(page)
        name = PTT_atc.name(page)
        DPnum = ptt.DW_pushnum(Pnum)                # ptt推文數處裡
        # 推文數大於？才下載
        if DPnum>95:
            print(DPnum, name,  '下載中...')
            domain = 'https://www.ptt.cc'
            ssoup = parse_url(domain, specific=True, href=url)
            # 判斷網址中有沒有圖片
            if len(ssoup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})) > 0:
                try:
                    # 將路徑cd到欲下載位置，並新增專屬資料夾
                    mk_exclusivedir(path, Pnum+name) # 創建專屬資料夾
                    for index, img_url in enumerate(ssoup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
                        try:
#                            print(name, index)
                            #記得更換下載的位置
                            urlretrieve(img_url['href'], path + '/{}/{}_{}.jpg'.format(Pnum+name ,name, index))
                        except:
                            print('url: {} {}_{}.jpg 下載失敗!'.format(img_url['href'], name, index))
                        finally:
                            del index
                except:
                    print('{} can not download {}'.format(name, page))
    print('{} finish'.format(name))
print('程式共花費:{:f}秒'.format(time.time() - start))
