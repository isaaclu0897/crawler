#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 00:14:26 2017

@author: wei
"""
from urllib.request import urlretrieve
import re
import time
from nbtool import change_page, parse_url, mk_exclusivedir, ptt

#三更，可按讚數下載, 及模組化

start = time.time()

# 目標頁
'''
page_target = str(input('請輸入你想下載的ptt網頁\nex:https://www.ptt.cc/bbs/Beauty/index2101.html\n>>>'))
page_number = int(input('請輸入想要下載的頁數\nex:2\n>>>'))
path = str(input('請輸入你想要存放的位置\nex:C:\\Users\\VX\\Downloads\\123123\n>>>'))
'''
page_target = 'https://www.ptt.cc/bbs/Beauty/index2102.html'
page_number = 5
path = '/home/wei/data/python'

count = 0
page_target = change_page.page(page_target, -1) # 換頁
# 跳轉到下一個頁面
while count<=page_number:
    page_target = change_page.page(page_target)
    count += 1
    soup = parse_url(page_target)   # 頁面解析
    # 進入到目標頁面中的每個主題頁面
    for page in soup.select('.r-ent'):
        likenumber = page.select('.nrec')[0].text
        name = page.select('a')[0].text
        likenum = ptt.deal_likenum(likenumber) # ptt推文數處裡
        # 推文數大於50才下載
        if likenum>50:
            print(likenum, name,  '下載中...')
            domain = 'https://www.ptt.cc'
            soup = parse_url(domain, specific=True, href=page.select('.title a')[0]['href'])
            # 判斷網址中有沒有圖片
            if len(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})) > 0:
                try:
                    # 將路徑cd到欲下載位置，並新增專屬資料夾
                    mk_exclusivedir(path, likenumber+name) # 創建專屬資料夾
                    for index, img_url in enumerate(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
                        try:
#                            print(type(img_url['href']))
#                            print(img_url['href'] + '...')
                            print(name, index)
                            #記得更改想要下載到的位置
                            urlretrieve(img_url['href'], path + '/{}/{}_{}.jpg'.format(likenumber+name ,name, index))
                        except:
                            print('url: {} {}_{}.jpg 下載失敗!'.format(img_url['href'], name, index))
                        finally:
                            del index
                except:
                    print('{} can not download {}'.format(name, page))
    print('{} finish'.format(name))
print('程式共花費:{:f}秒'.format(time.time() - start))

