#简洁,表达字符串的特征
import re
ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
for item in ls:
    print(item)