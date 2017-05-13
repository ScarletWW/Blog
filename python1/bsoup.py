#encoding=utf-8
import requests
from bs4 import BeautifulSoup#将字符串转换成utf-8

r=requests.get("http://python123.io/ws/demo.html")
#print(r.text)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
#print(soup.prettify())
#print(soup.a)
tag = soup.a
#print(tag.attrs['href'])
#print(soup.a.next_sibling.next_sibling)
#print(soup.prettify())#清晰显示标签
soup.p.string='中文'
print(soup.p.prettify())