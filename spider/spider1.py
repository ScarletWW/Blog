#!/usr/bin/python
#encoding=utf-8

import requests
url = "http://www.baidu.com/s"
keyword="Python"
try:
    kv={'wd':keyword}
    r = requests.get(url,params=kv)
    print(r.request.url)
    print(r.request.headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    #print(r.text[1000:2000])
except:
    print("爬取失败")


