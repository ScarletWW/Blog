#!/usr/bin/python
#encoding=utf-8
import requests
from bs4 import BeautifulSoup
import re
r=requests.get("http://python123.io/ws/demo.html")
#print(r.text)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
#print(soup.title.contents)
#便签树的遍历方法
#print(soup.contents)
#信息标记html超文本标记语言，将超文本信息嵌入到文本当中
#xml扩展标记语言，通过标签来构建信息
#for link in soup.find_all('a'):
#	print(link.get('href'))
#for link in soup.find_all(True):	
#	print(link.name)
#for link in soup.find_all(re.compile('b')):
#	print(link.name)
for link in soup.find_all(text = re.compile('Python')):
	print(link)



