# bs是一个高效的网页解析库
# 类似于前端开发的数模转换，可以讲一个网页内容，转换成一个soup对象，然后我们直接访问标签内容

from bs4 import BeautifulSoup


html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc, 'lxml')
# 获取某个节点的文本
print(soup.title.string)
print(soup.p.string)
# 获取某个节点父节点的文案
print(soup.title.parent.name)

# 获取某个节点
print(soup.a)
# 获取全部某节点
print(soup.find_all('a'))
