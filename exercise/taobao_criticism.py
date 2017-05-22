import requests
import re
from bs4 import BeautifulSoup
import json

def getHTMLTest(url, data):
    try:
        r = requests.get(url, params=data, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def paserComments(html):
    try:
        html = re.search(r'(?<=fetchJSON_comment98vv158\().*(?=\);)', html).group(0)
    except:
        print("")
    j = json.loads(html)
    ilt = j['comments']
    for comment in ilt:
        c_content = comment['content']
        c_time = comment['referenceTime']
        c_name = comment['nickname']
        c_client = comment['userClientShow']
        print('{} {} {}\n{}\n'.format(c_name, c_time, c_client, c_content))

def main():
    start_url = 'https://club.jd.com/comment/productPageComments.action'
    data = {
        "callback":"fetchJSON_comment98vv158",
        "productId":"4350840",
        "score":0,
        "sortType":5,
        "page":0,
        "pageSize":10,
        "isShadowSku":0
    }
    depth = 3
    for i in range(depth):
        try:
            data["page"]=i
            html = getHTMLTest(start_url, data)
            #print(html)
            paserComments(html)
        except:
            continue
if __name__ == '__main__':
    main()