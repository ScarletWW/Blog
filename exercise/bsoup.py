from bs4 import BeautifulSoup
import requests
import re
import json
"""
callback:fetchJSON_comment98vv158
productId:4350840
score:0
sortType:5
page:3
pageSize:10
isShadowSku:0
"""
url = 'https://club.jd.com/comment/productPageComments.action'
data = {
        'callback':'fetchJSON_comment98vv158',
        'productId':'4350840',
        'score':0,
        'sortType':5,
        'page':0,
        'pageSize':10,
        'isShadowSku':0
    }
html_doc = """
                             <div style="display: none"><a href="//cps.jd.com">销售联盟</a><a href="//gongyi.jd.com">京东公益</a><a href="//club.jd.com/links.aspx">友情链接</a>
            <div id="hidcomment">
            <div class="item">
        <div class="user"><div class="u-address">()</div><div class="date-buy">购买日期<br>2017-03-20</div></div>
        <div class="i-item"><div class="o-topic"><strong class="topic"><a href="//club.jd.com/repay/4350840_ecd233f0-3b7a-49cf-bc88-a58477e77047_1.html">京东改咸鱼了。全新的错版键盘！问：键盘是新的么？答：京东注重质量，保证真品。我勒个擦，看不懂中国话啊！我说你卖假货了么？</a></strong><span class="star sa5"></span><span class="date-comment">2017-03-20 11:37:01</span></div><div class="comment-content">使用心得：京东改咸鱼了。全新的错版键盘！问：键盘是新的么？答：京东注重质量，保证真品。我勒个擦，看不懂中国话啊！我说你卖假货了么？</div></div>
      </div>
            <div class="item">
        <div class="user"><div class="u-address">()</div><div class="date-buy">购买日期<br>2017-05-09</div></div>
        <div class="i-item"><div class="o-topic"><strong class="topic"><a href="//club.jd.com/repay/4350840_86bdc52c-034e-45c3-8fd1-ca1bea8fdec9_1.html">还是没搞懂怎么开启mac快捷键，怎么就看不懂这说明书了&hellip;&hellip;键是好键</a></strong><span class="star sa5"></span><span class="date-comment">2017-05-09 12:13:16</span></div><div class="comment-content">使用心得：还是没搞懂怎么开启mac快捷键，怎么就看不懂这说明书了&hellip;&hellip;键是好键</div></div>
      </div>
            <div class="item">
        <div class="user"><div class="u-address">()</div><div class="date-buy">购买日期<br>2017-04-02</div></div>
        <div class="i-item"><div class="o-topic"><strong class="topic"><a href="//club.jd.com/repay/4350840_34bd683a-1ec8-4378-a17e-f4ec6c60c27a_1.html">经过测试 基本能配合Mac用，我把cmd和alt对调位置后 再按fn+pause切换为Mac键位，然后再按fn+end保存即可，这样就不怕重新插拔的时候恢复默认了，待机唤醒没问题 f区也完全可用 这个做法连修饰键都不用改 爽爽的。</a></strong><span class="star sa5"></span><span class="date-comment">2017-04-02 00:24:34</span></div><div class="comment-content">使用心得：经过测试 基本能配合Mac用，我把cmd和alt对调位置后 再按fn+pause切换为Mac键位，然后再按fn+end保存即可，这样就不怕重新插拔的时候恢复默认了，待机唤醒没问题 f区也完全可用 这个做法连修饰键都不用改 爽爽的。</div></div>
      </div>
            <div class="item">
        <div class="user"><div class="u-address">()</div><div class="date-buy">购买日期<br>2017-05-03</div></div>
        <div class="i-item"><div class="o-topic"><strong class="topic"><a href="//club.jd.com/repay/4350840_2ad50df9-5fa0-4df5-9b9a-e99fcf67424b_1.html">白色键盘和Macbook是最搭配的了。键盘手感不错。灵敏度比较高。红轴声音小点。把command键和Alt键相互切换。就能完美兼容Mac了。不需要额外的设置。Mac的完美小伙伴！</a></strong><span class="star sa5"></span><span class="date-comment">2017-05-03 22:01:35</span></div><div class="comment-content">使用心得：白色键盘和Macbook是最搭配的了。键盘手感不错。灵敏度比较高。红轴声音小点。把command键和Alt键相互切换。就能完美兼容Mac了。不需要额外的设置。Mac的完美小伙伴！</div></div>
      </div>
"""
r = requests.get(url, params=data)
r.raise_for_status()
r.encoding = r.apparent_encoding
#print(len(r.text))
html = r.text
#print(type(html))
try:
    html = re.search(r'(?<=fetchJSON_comment98vv158\().*(?=\);)', html).group(0)
except:
    print("")
j = json.loads(html)
commentsSummary = j['comments']
for comment in commentsSummary:
    c_content = comment['content']
    c_time = comment['referenceTime']
    c_name = comment['nickname']
    c_client = comment['userClientShow']
    print('{} {} {}\n{}\n'.format(c_name,c_time,c_client,c_content))
#print(soup.prettify())
#print(soup.find_all("a",{"class":"sister"}))
#com = soup.find_all("strong",{"class":"topic"})
#data = soup.find_all("div",{"class":"date-buy"})
#coms = re.findall(r'(?<=购买日期<br>)[\d]{4}\-[\d]{2}\-[\d]{2}', html)
#print(coms)