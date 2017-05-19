class Student(object):
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return 'Student object (name: %s)' % self._name
    __repr__ = __str__
print(Student('Jack'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0 , 1

    def __iter__(self):
        return self

    def __getitem__(self, item):
        if isinstance(item, int): # n为索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice): # 实现切片功能
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            L = []
            a, b = 1, 1
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

    def __next__(self):
        self.a , self.b = self.b, self.a+self.b
        if self.a > 10000:
            raise StopIteration
        return self.a
#for n in Fib():
#    print(n)
f= Fib()
print(f[5])
print(f[5:10])
