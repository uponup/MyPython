

class Test:
    def __init__(self, x):
        self.data = x

    def prt(self):
        print(self)
        print(self.__class__)

    def printData(self):
        print(self.data)
t = Test(10)
t.prt()
t.printData()

# ⚠️注意：self不是python的关键字


# 继承
class people:
    name = ''
    age = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s 说： 我 %d 岁'%(self.name, self.age))

class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    
    def speak(self):
        print("%s 说：我今年 %d 岁了，我在 %d 年级读书"%(self.name, self.age, self.grade))


std1 = student('Tom', 12, 80, 6)

std1.speak()


# 多继承
# 方法重写
# 类属性与方法
    # 私有属性：__privateName：以两个下划线开头
    # 私有方法：__privateMethod