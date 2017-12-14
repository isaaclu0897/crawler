#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:26:30 2017

@author: wei
"""

from urllib.request import urlretrieve
import re
import time
from nbtool import change_page, parse_url, mk_exclusivedir, ptt
import gevent
from gevent import monkey;
monkey.patch_all()         #添加io操作标准，让程序可以并行下载网页

def download_img(index, img_url, path, likenumber, name):
    try:
#        print(type(img_url['href']))
#        print(img_url['href'] + '...')
        #記得更改想要下載到的位置
#        print(name, index, 'downloading')
        urlretrieve(img_url['href'], path + '/{}/{}_{}.jpg'.format(likenumber+name ,name, index))
#        print(name, index, 'finish')
    except Exception as e:
        print('url: {} {}_{}.jpg 下載失敗!'.format(img_url['href'], name, index))
    finally:
        del index

def subpage(page): 
#    try:
#    if page.select('.meta .aauthor')[0].text != '-':
        likenumber = page.select('.nrec')[0].text
        name = page.select('a')[0].text
        likenum = ptt.deal_likenum(likenumber) # ptt推文數處裡
        # 推文數大於50才下載
        if likenum>90:
    #        print(likenum, name,  '下載中...')
            domain = 'https://www.ptt.cc'
            soup = parse_url(domain, specific=True, href=page.select('.title a')[0]['href'])
            # 判斷網址中有沒有圖片
            if len(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})) > 0:
                try:
                    # 將路徑cd到欲下載位置，並新增專屬資料夾
                    mk_exclusivedir(path, likenumber+name) # 創建專屬資料夾
                    for index, img_url in enumerate(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
                        task = [gevent.spawn(download_img, index, img_url, path, likenumber, name)]
                    gevent.joinall(task)
                except:
                    print('{} can not download {}'.format(name, page))
#    except:
#        print('error')
def mainpage(page_target):           
#    try:
        soup = parse_url(page_target)   # 頁面解析
        # 進入到目標頁面中的每個主題頁面
        for page in soup.select('.r-ent'):
            task = [gevent.spawn(subpage, page)]
        gevent.joinall(task)
    #    print('{} finish'.format(name))
#    except:
#        print('error2')

if __name__ == '__main__':
    #五更，gevent封裝mainpage, subpage, download_img
    start = time.time()
    
    # 目標頁
    '''
    page_target = str(input('請輸入你想下載的ptt網頁\nex:https://www.ptt.cc/bbs/Beauty/index2101.html\n>>>'))
    page_number = int(input('請輸入想要下載的頁數\nex:2\n>>>'))
    path = str(input('請輸入你想要存放的位置\nex:C:\\Users\\VX\\Downloads\\123123\n>>>'))
    '''
    page_target = 'https://www.ptt.cc/bbs/Beauty/index2000.html'
    page_number = 10
    path = '/home/wei/data/python/ptt_photo'
    n = 0
    while n <= 270:
        count = 0
        page_target = change_page.page(page_target, -1) # 換頁
        # 跳轉到下一個頁面
        while count<=page_number:
            page_target = change_page.page(page_target)
            count += 1
            task = [gevent.spawn(mainpage, page_target)]
        gevent.joinall(task)
        print('程式共花費:{:f}秒'.format(time.time() - start))
        n += 1
        time.sleep(5)