
# 1、异常检测：try...except...

# while True:
#     try:
#         x = int(input("请输入一个数字"))
#         break
#     except ValueError:
#         print('您输入的不是数字, 请尝试再次输入')

# while True:
#     try:
#         x = int(input("请输入一个数字"))
#         break
#     except ValueError:
#         print('您输入的不是数字, 请尝试再次输入')
#     else:
#         print("输入成功！", x)


# try:
#     print('try')
# except:
#     print('异常')
# else: 
#     print('没有异常')
# finally:
#     print('这句话无论如何都会执行')



# 2、抛出异常：raise

x = 10

if x > 5:
    raise Exception('x 不能大于5， 当前x的值为:{}'.format(x))


# 3、自定义异常