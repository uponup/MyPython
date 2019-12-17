
# 在Python中，变量是没有类型的，类型属于对象。
# 变量仅仅是一个对象的引用（一个指针），可以指向List对象，也可以指向String对象

def changeValue(a):
    a[2] = 'C'

a = [1, 2, 3, 4]

changeValue(a)

print(a)
