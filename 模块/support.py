def print_func(param):
    print(param)

# 第一次被引入的时候，主程序将运行。区分是在当前模块执行，还是被引入的模块执行
if __name__ == '__main__':
    print("程序自身在运行")
else:
    print('我来自另一个模块')