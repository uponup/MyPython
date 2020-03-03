
# 在Python中，变量是没有类型的，类型属于对象。
# 变量仅仅是一个对象的引用（一个指针），可以指向List对象，也可以指向String对象

def changeValue(a):
    a[2] = 'C'

a = [1, 2, 3, 4]

# Python中的函数参数，分为可变类型和不可变类型（可以理解为引用类型和值类型）。如List、字典等就是可变类型，函数中对参数的修改会影响到函数外。
changeValue(a)
print(a)
