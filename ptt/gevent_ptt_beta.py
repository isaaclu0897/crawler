#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:26:30 2017

@author: wei
"""

from urllib.request import urlretrieve
import re
import time
from nbtool import change_page, parse_url, mk_exclusivedir, ptt, PTT_atc
import gevent
from gevent import monkey;  monkey.patch_all()

def download_img(index, Iurl, path, Pnum, Fname):
    try:
        #記得更改想要下載到的位置
#        print(Fname, index, 'downloading')
        urlretrieve(Iurl['href'], path + '/{}/{}_{}.jpg'.format(Pnum+Fname ,Fname, index))
#        print(Fname, index, 'finish')
    except Exception as e:
        print('url: {} {}_{}.jpg 下載失敗!'.format(Iurl['href'], Fname, index))
    finally:
        del index

def subpage(page): 
        Pnum = PTT_atc.push_num(page)
        url = PTT_atc.url(page)
        Fname = PTT_atc.name(page)
        DPnum = ptt.DW_pushnum(Pnum) # ptt推文數處裡
        # 推文數大於？才下載
        if DPnum>90:
            print(DPnum, Fname,  '下載中...')
            domain = 'https://www.ptt.cc'
            soup = parse_url(domain, specific=True, href=url)
            # 判斷網址中有無圖片
            if len(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})) > 0:
                try:
                    # 將路徑cd到欲下載位置，並新增專屬資料夾
                    mk_exclusivedir(path, Pnum+Fname) # 創建專屬資料夾
                    for index, img_url in enumerate(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
                        task = [gevent.spawn(download_img, index, img_url, path, Pnum, Fname)]
                    gevent.joinall(task)
                except:
                    print('{} can not download {}'.format(Fname, page))
#            print('\t\t', DPnum, Fname,  '下載完畢')

def mainpage(page_target):           
        soup = parse_url(page_target)   # 頁面解析
        # 進入到目標頁面中的每個主題頁面
        for page in soup.select('.r-ent'):
            task = [gevent.spawn(subpage, page)]
        gevent.joinall(task)
#        print('{} finish'.format(name))

if __name__ == '__main__':
    #五更，gevent封裝mainpage, subpage, download_img
    start = time.time()
    
    # 目標頁
    '''
    page_target = str(input('請輸入你想下載的ptt網頁\nex:https://www.ptt.cc/bbs/Beauty/index2101.html\n>>>'))
    page_number = int(input('請輸入想要下載的頁數\nex:2\n>>>'))
    path = str(input('請輸入你想要存放的位置\nex:C:\\Users\\VX\\Downloads\\123123\n>>>'))
    '''
    page_target = 'https://www.ptt.cc/bbs/Beauty/index2102.html'
    page_number = 20
    path = '/home/wei/data/python/ptt_photo'
   
    count = 0 
    page_target = change_page.page(page_target, -1, printu=False)     # 換頁
    # 跳轉到下一個頁面
    while count<=page_number:
        page_target = change_page.page(page_target)
        count += 1
        soup = parse_url(page_target)   # 頁面解析
        # 進入到目標頁面中的每個主題頁面
        for page in soup.select('.r-ent'):
            task = [gevent.spawn(subpage, page)]
        gevent.joinall(task)
        print()
    print('程式共花費:{:2f}秒'.format(time.time() - start))
