

with open("/Users/wanghaotian/Documents/Blog/exercise/read.txt", "r") as f:
    for line in f.readlines():
        print(line.strip()) # 把/n去掉
with open("/Users/wanghaotian/Documents/Blog/exercise/read.txt", "a") as f:
    f.write("\n王浩天")
"""
读取非字符文件
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'
"""