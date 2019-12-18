
import support
from fibo import fibo, fibo2
import sys

support.print_func('调用模块的方法')

fibo(10)
print('\n')
fibo2(10)


# from package import item
# 使用这种方式导入的时候，item既可以是子模块，也可以是函数、类或者变量

# import package.item
# 使用这种方式导入的时候，除类最后一项，其他的必须为包，最后一项则可以是模块或者包。但是不能为函数、类或者变量

