import re

pattern = 'com$'
print(re.search( pattern, 'www.baidu.com', flags=0))


# group() 匹配对象的方法
line = "Dogs are smarter than cats"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


# re.match 和 re.search的区别:
# match只是匹配字符串的开始
# seach会匹配整个字符串，直到找到一个匹配

# matchObj = re.match( r'cats', line, re.M|re.I)
# if matchObj:
#     print('match -->:', matchObj.group())
# else:
#     print('No match！')

# matchObj = re.search( r'cats', line, re.M|re.I)
# if matchObj:
#     print('search -->:', matchObj.group())
# else:
#     print('No search')





# 检索和替换
# Python的re模块中提供了re.sub用于替换字符串的匹配项

phone = "+86 17611102431 #这是一个电话好吗"

pattern = "#.*$"
num = re.sub( pattern, "", phone)
print("1、电话号码：", num)

# 移除非数字的内容
num = re.sub( r'\D', "", phone)
print("2、电话号码：", num)





# compile
# re.compile 用于生成一个正则对象

# findall
# 匹配所有，match和search都是匹配一次，而findall是匹配所有





# 正则表达式修饰符
# re.I        对大小写不敏感
# re.L        本地化识别匹配
# re.M        多行匹配
# re.S        使.匹配包括换行在内的所有字符
# re.U        使用Unicode字符集解析字符
# re.X        灵活格式
