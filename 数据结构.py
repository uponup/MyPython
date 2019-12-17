#列表
'''
.append(x)
.extend(L)
.insert(i, x)
.remove(x)
.pop([i])       //i两边的括号代表这个参数是可选的
.clear()        //移除所有项
.index(x)       //返回第一个值为x的元素的索引
.count(x)       //返回x在列表中出现的次数
.sort()         //对列表中的元素进行排序
.reverse()      //倒排列表中的元素
.copy()         //返回列表的浅复制
'''

# 列表推导式
# 格式：for 后面跟一个表达式

vec = [1, 2, 3, 4, 5, 6]

list = [x for x in vec]
list1 = [x for x in vec if x > 3]
list2 = [x*2 for x in vec if x > 3]
print(list)
print(list1)
print(list2)