class Student(object):
    __slots__ = ('name','age') # 限制实例的属性

    def set_age(self, age):
        self.age = age
def set_name(self,name):
    self.name = name

if __name__ == '__main__':
    s = Student()
    s.set_age(20)
    s.name = 'Mike'
    Student.set_name = set_name # 给Student类绑定方法
    s.set_name('James')
    print(s.name,s.age)
