#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 01:42:07 2017

@author: wei
"""

 
from bs4 import BeautifulSoup as bf

class PTT_article(object):
    
    def __init__(self, soup):
        self.url = soup.select('a')[0]['href']
        self.name = soup.select('a')[0].text
        self.date = soup.select('.date')[0].text
        self.author = soup.select('.author')[0].text
        self.push_num = soup.select('.nrec')[0].text
        
if __name__ == '__main__':
    test_html = '''<div class="r-ent"><div class="nrec"><span class="hl f3">39</span></div><div class="mark"></div><div class="title"><a href="/bbs/Beauty/M.1490582140.A.B96.html">[正妹] 神等級 絕不“虎”爛</a></div><div class="meta"><div class="date"> 3/27</div><div class="author">TWpower5566</div></div></div>'''
    soup = bf(test_html, 'lxml')
    for soup in soup.select('.r-ent'):        
        atc = PTT_article(soup)
        print(atc.url, atc.name, atc.date, atc.author, atc.push_num)