
# input内置函数
# str = input("请输入：")
# print("您输入的内容是：", str)


# 读写文件
# open()将会返回一个file对象，基本语法格式：
# open(filename, mode)      //mode默认为只读

f = open('/tmp/foo.txt', 'w')
f.write("Python 是一门非常好的语言。\n是的，的确非常好！\n")
f.close()

# 文件对象的方法

# 1、f.read()
f = open('/tmp/foo.txt', "r")
str = f.read()
print(str)
f.close()

# 2、f.readline()       //只读一行
f = open('/tmp/foo.txt', "r")
linestr = f.readline()
print(linestr)
f.close()

# 3、f.readlines()      //读取多行
f = open('/tmp/foo.txt', "r")
linesStr = f.readlines()
print(linesStr)
f.close()

# 4、f.write()将string写入到文件中，返回字数
f = open('/tmp/foo.txt', "w")
num = f.write("宫城，今天你将面对的是亚洲第一控卫，你知道这意味着什么吗？\n打败他，我就是第一了！")
print(num)
f.close()

# 5、f.tell()   返回文件对象当前所处的位置
# 6、f.seek()   改变当前文件位置0:开头，1:当前位置，2:结尾
# 7、f.close()




# pickle模块
import pickle

# 使用pickle模块将数据对象保存到文件中
data1 = { 'a': [1, 2.0, 3, 4+6j],
          'b': ('String', u'Unicode String'),
          'c': None }
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0
# pickle.dump(data1, output)

# Pickle the list using the highest protoco available
pickle.dump(selfref_list, output, -1)
output.close()


import pprint
# 使用pickle模块从文件中读取数据对象
pkl_file = open('data.pkl', 'rb')

# data1_1 = pickle.load(pkl_file)
# pprint.pprint(data1_1)

data2_2 = pickle.load(pkl_file)
pprint.pprint(data2_2)

pkl_file.close()


