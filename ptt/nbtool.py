#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:12:58 2017

@author: wei
"""
import os
import requests 
from bs4 import BeautifulSoup

class change_page():
    ''' 換頁函數
    
    說明: 抽取 url 的 index 置換成下個頁面的 index
    '''
    def index(url, index, printu=True):
        ''' 索引換頁
        
        換到第2312頁
        ex: url = 'https://www.ptt.cc/bbs/Beauty/index2102.html'
            change_page.index(url, 2312)
            
            # https://www.ptt.cc/bbs/Beauty/index2312.html
        '''
        if not str(index).isdigit():
            print(123)
        url = url.split('/')
        url[-1] = ('index{}.html'.format(index))
        url = '/'.join(url)
        if printu:
            print(url)
        return url
    def page(url, jump_page=1, printu=True):
        ''' 頁數換頁
       
        換1頁
        ex: 
            url = 'https://www.ptt.cc/bbs/Beauty/index2102.html'
            change_page.page(url)
            
            # https://www.ptt.cc/bbs/Beauty/index2103.html
        換3頁
        ex: 
            url = 'https://www.ptt.cc/bbs/Beauty/index2102.html'
            change_page.page(url, 3)
            
            # https://www.ptt.cc/bbs/Beauty/index2105.html
        向前換2頁
        ex: 
            url = 'https://www.ptt.cc/bbs/Beauty/index2102.html'
            change_page.page(url, -2)
            
            # https://www.ptt.cc/bbs/Beauty/index2100.html
        '''            
        index = str(int(''.join([index_num for index_num in url if index_num.isdigit()])) + jump_page) 
        url = url.split('/')
        url[-1] = ('index{}.html'.format(index))
        url = '/'.join(url)
        if printu:
            print(url)
        return url
    
def parse_url(url, specific=False, href=None):
    ''' 解析網頁內容
    
    說明: 將 url 轉換成 html 以便抽取
    -----
    解析給定網頁
    ex: url = 'https://www.ptt.cc/bbs/Beauty/index2102.html'
        pares_url(url)
        
        擷取
        #   <div class="r-ent">
            <div class="nrec"><span class="hl f1">爆</span></div>
            <div class="mark"></div>
            <div class="title">
            <a href="/bbs/Beauty/M.1490441716.A.0CA.html">[正妹] 假日合輯</a>
            </div>
            <div class="meta">
            <div class="date"> 3/25</div>
            <div class="author">Kyle5566</div>
            </div>
            </div>
    解析給定網域及特定子題
    ex: domain = 'https://www.ptt.cc'
        specific_url = '/bbs/Beauty/M.1490441716.A.0CA.html'
        parse_url(domain, specific=True, href=specific_url)
        
        擷取
        #   <a href="http://i.imgur.com/snPJtnI.jpg" rel="nofollow" target="_blank">http://i.imgur.com/snPJtnI.jpg</a>
            <a href="http://i.imgur.com/MGyzVsn.jpg" rel="nofollow" target="_blank">http://i.imgur.com/MGyzVsn.jpg</a>
            <a href="http://i.imgur.com/HsgmPx2.jpg" rel="nofollow" target="_blank">http://i.imgur.com/HsgmPx2.jpg</a>
            <a href="http://i.imgur.com/nBaQ1Rn.jpg" rel="nofollow" target="_blank">http://i.imgur.com/nBaQ1Rn.jpg</a>
            <a href="http://i.imgur.com/L369uMP.jpg" rel="nofollow" target="_blank">http://i.imgur.com/L369uMP.jpg</a>
            <a href="http://i.imgur.com/zlVGsFX.jpg" rel="nofollow" target="_blank">http://i.imgur.com/zlVGsFX.jpg</a>
            <a href="http://i.imgur.com/Psw6R1v.jpg" rel="nofollow" target="_blank">http://i.imgur.com/Psw6R1v.jpg</a>
            <a href="http://i.imgur.com/wMwkOcm.jpg" rel="nofollow" target="_blank">http://i.imgur.com/wMwkOcm.jpg</a>
            <a href="http://i.imgur.com/FpvANo2.jpg" rel="nofollow" target="_blank">http://i.imgur.com/FpvANo2.jpg</a>
    '''
    if specific == True:
        url += href
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    del res
    return soup

def mk_exclusivedir(path, dirname):
    ''' 創見專屬資料夾
    
    說明: 在路徑 path 中, 創見名為 dirname 的資料夾
    -----
    ex: 
        path = '/home/wei/data/python/photo'
        dirname = 'good'
        os.path.isdir(path + '/' + dirname) # False
        mk_exclusivedir(path, dirname)
        os.path.isdir(path + '/' + dirname) # True
    '''
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)
    if not os.path.isdir(dirname):
        os.mkdir('{}'.format(dirname))
class ptt():
    ''' ptt特定函數
    '''
    def DW_pushnum(obj):
        ''' ptt推文數處裡
        
        說明: ptt 推文數會有文字"爆"及"空", 需要處理掉才能過濾讚數
        '''
        try:
            pushnum = int(obj)
        except:
            if obj == '爆':
                pushnum = 99
            elif obj == '':
                pushnum = -10
            elif obj == 'X1':
                pushnum = -200
            else:
                pushnum = 0
        return pushnum
    
class PTT_atc():
    def name(block):
        return block.select('a')[0].text 
        
    def url(block):
        return block.select('a')[0]['href']
        
    def date(block):
        return block.select('.date')[0].text
        
    def author(block):
        return block.select('.author')[0].text
    
    def push_num(block):
        return block.select('.nrec')[0].text


