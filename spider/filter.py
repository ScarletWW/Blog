#!/usr/bin/python
#encoding=utf-8
#碰到yield直接返回函数调用的位置,不执行以下代码,当再次调用函数.next()时,开始从yield处执行
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n #先把所有的奇数找到

def _not_divisible(n):
    return lambda x: x % n > 0 #再使用filter过滤器把list中能整除前面的数去掉

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
if __name__ == '__main__':
    main()