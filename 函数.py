
# 函数：
def hello():
    print("hello world!")

hello()



# 在Python中，变量是没有类型的，类型属于对象。
# 变量仅仅是一个对象的引用（一个指针），可以指向List对象，也可以指向String对象

def changeValue(a):
    a[2] = 'C'

a = [1, 2, 3, 4]
changeValue(a)
print(a)

#参数
# 必需参数
def printMe(str):
    print(str)
    return

printMe("必须参数")

# 关键字参数
def printMe2(str):
    print(str)

printMe2(str = "关键字参数")

def printInfo(name, age):
    print("名字", name, "年龄", age)

printInfo(age= "12", name="Tom")
printInfo(name= "Bob", age="13")

# 默认参数

def printInfo2(name, age = 0):
    print("名字", name, "年龄", age)

printInfo2("Tony")

# 不定长参数
# 带一个*号的参数，会以一个元组的形式传进来
def printInfo3(name, *varTuple):
    print("输出", name, varTuple)

printInfo3('Jerry', 10, 23, 34, 55)

# 带两个*号的参数
def printInfo4(name, **varDict):
    print(varDict)
    
printInfo4('Mary', a=2, b=3, c='Tom')



# 匿名函数
# 使用关键字lambda

sum = lambda arg1, arg2: arg1 + arg2

print("两个数相加后为：", sum(10, 20))
print("两个数相加后为：", sum(20, 20))


# return语句
def sum2(arg1, arg2, arg3):
    return arg1 + arg2 + arg3
print(sum2(1, 2, 3))
