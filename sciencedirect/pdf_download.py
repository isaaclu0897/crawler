# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:54:26 2017

@author: VX
"""

import os
import requests
from bs4 import BeautifulSoup


file_dir = '/home/wei/good/'
os.chdir(file_dir)
print(os.getcwd())

#user_agent = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

src_url_root = "https://www.sciencedirect.com/"
src_url_index = "science/article/pii/S0196890417312529/pdfft?md5=35c74e25a68fa11610eb1ef49ff8be12&pid=1-s2.0-S0196890417312529-main.pdf"
src_url = src_url_root + src_url_index
src_res = requests.get(src_url, stream=True)
soup = BeautifulSoup(src_res.content, "lxml")
paper_url = soup.body.div.p.a['href']

#print(download_url)
##file_name = download_url.split('/')[-1]

paper_res = requests.get(paper_url, stream=True)
file_name = 'll.pdf'
with open(file_name, 'wb') as f:
    f.write(paper_res.content)
print("Completed")


