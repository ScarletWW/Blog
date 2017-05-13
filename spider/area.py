#!/usr/bin/python
#encoding=utf-8

import requests
import re
from bs4 import BeautifulSoup
url = "https://zhidao.baidu.com/question/570927112.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
demo=r.text
soup = BeautifulSoup(demo,"html.parser")
#	print(link.name)
for link in soup.find_all(text = re.compile('area')):
	print(link)
#print(soup.prettify())
