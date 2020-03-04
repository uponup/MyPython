
# \       转义字符
# ^       匹配开始位置
# $       匹配结束位置
# *       匹配前一个字符0次或者n次
# +       匹配前一个字符1词或者多次
# ？      匹配前一个字符0词或者1次
# {n}     匹配确定的n次，n为非负整数
# {n,}    至少匹配n次数
# {n, m}  至少匹配n次，但是至多匹配m次
# [xyz]   字符集合，匹配所包含的任意字符
# [^xyz]  排除字符集合
# [a-z]   字符范围
# [^a-z]  排除字符范围
# \b      匹配单词边界     例如er\b 可以匹配never中的er，但是不能匹配verb中的er
# \B      匹配非单词边界   例如er\b 可以匹配verb中的er
# \d      匹配一个数字
# \D      匹配一个非数字字符
# \f      匹配一个换页符
# \n      匹配一个换行符
# \r      匹配一个回车符
# \t      匹配一个制表符
# \s      匹配任何空白符
# \S      匹配任何非空白符
# \v      匹配一个垂直制表符
# \w      代表字母，下划线，数字
# \W      非字母，下划线，数字
# \xnn    16进制

import re

text = "longge de  phone is +17611102431 s"
# 匹配数字
res = re.match(r'^lo.*(\d+)\s.*s$', text)
print(res.group(1))

# 非贪婪匹配，得到所有的数字
res = re.match(r'^lo.*?(\d+)\s.*s$', text)
print(res.group(1))

# .*?中的.代表所有字符，那如果出现\n \r等换行字符怎么办呢？这时候我们就用到了re的匹配模式呀，例如：
content = """longge de  phone is +17611102431
 s"""
res = re.match(r'^lo.*?(\d+)\s.s$', content, re.S)
print(res.group(1))

# 以上我们正则表达式中，都是以^开头，以$结尾的，我们可以利用re的另外一个方法search，不使用开头和结尾的符号
res = re.search(r'^lo.*?(\d+)\s.s', content, re.S)
print(res.group(1))

# 但是如果字符串中有多个数字字符串呢，这时候我们就得利用re的另外一个方法findall
content = """longge de  phone is +17611102431 s;
longge de  phone is +17611102431 s;
longge de  phone is +17611102431 s;
longge de  phone is +17611102431 s;"""
res = re.findall(r'lo.*?(\d+)\s.*?s;', content, re.S)
print(res)


# 现在需求变了，我们想把刚刚找到的电话好吗替换，这时候我们就用到了re的sub方法
content = re.sub(r'\d+', '1387789902', content)
print(content)


# 最后再提一下re的另外一个方法，compile，这个方法主要把制表符封装了一下
