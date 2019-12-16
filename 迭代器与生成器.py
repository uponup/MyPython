import sys
list = [1, 2, 3, 5, 6]

it = iter(list)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


# 创建一个迭代器
# StopIteration异常 用于标识迭代的完成

# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
    
# myClass = MyNumber()
# myiter = iter(myClass)

# count = 0
# while count < 10000:
#     try:
#         count = next(myiter)
#         print(count)
#     except StopIteration:
#         sys.exit()




# 生成器
# 在Python中，使用类yeild函数，被称为生成器。生成器是一个返回迭代器的函数，简单理解生成器就是一个迭代器。

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()
