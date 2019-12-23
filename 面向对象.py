


def main0():
    arr1 = [(suite, face) for suite in '♠️♥️♣️♦️' for face in range(1, 4)]
    arr2 = [(suite, face) for suite in '♠♥♣♦' for face in range(1, 4)]

    for (suite, face) in arr1:
        print(suite, face)

    print('\n=====================\n')

    for (suite, face) in arr2:
        print(suite, face)

if __name__ == '__main__':
    main0()



class Test:
    def __init__(self, x):
        self.data = x
        self.__count = x + 1

    def prt(self):
        print(self)
        print(self.__class__)

    def printData(self):
        print(self.data)
t = Test(10)
t.prt()
t.printData()

# 私有 Tips：
# 1、Python其实并没有从语法上严格保证私有属性和方法的私密性，如果我们知道私有成员变量的名字，依旧可以访问到。如下：
print(t._Test__count)
# 2、实际开发中，我们并不建议将属性设置为私有的，因为这回导致子类无法访问。我们会遵循一种命名惯例，就是让属性名以单下划线的开头来表示属性是收保护的






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






# @property 装饰器
# 同OC类似，我们可以使用@property关键字来修饰属性，分别实现属性的getter和setter方法

class Animal(object):
    def __init__(self, age, name):
        self._age = age
        self._name = name

    @property 
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, age):
        self._age = age

def main():
    dog = Animal(2, 'Peper')
    dog.age = 3
    # dog.name = 'Flask'            # 没有实现name的setter方法，所以赋值失败

if __name__ == '__main__':
    main()




# 静态方法和类方法
# @staticmethod
# @classmethod



# 多态
from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_vioce(self):
        pass


class Dog(Pet):
    def make_vioce(self):
        print('%s：汪汪汪' %self._nickname)
    
class Cat(Pet):
    def make_vioce(self):
        print('%s: 喵喵喵' %self._nickname)


def main2():
    pets = [Dog('旺财'), Cat('凯蒂')]
    for pet in pets:
        pet.make_vioce()


if __name__ == '__main__':
    main2()