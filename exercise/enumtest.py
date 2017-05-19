from enum import Enum, unique
#注意一定不要把文件名定义成标准库模块的名字
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#for name, member in Month.__members__.items():
#    print(name, '=>', member, ',', member.value) # value属性则是自动赋给成员的int常量，默认从1开始计数。

@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday(1))
for name,member in Weekday.__members__.items():
    print(name, '=>', member)
