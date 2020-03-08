import csv

with open('./python爬虫/xiaoshuaib.csv', mode='w') as csv_file:
    fieldnames = ['你是谁', '你几岁', '你多高']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'你是谁': '小帅b', '你几岁': '18岁', '你多高': '18cm'})
    writer.writerow({'你是谁': '小帅c', '你几岁': '19岁', '你多高': '17cm'})
    writer.writerow({'你是谁': '小帅d', '你几岁': '20岁', '你多高': '16cm'})


with open('./python爬虫/uponup.csv', mode='w') as csv_file:
    fieldnames = ['姓名', '年龄', '身高', '体重']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'姓名': 'Tom', '年龄': '12', '身高': '176cm', '体重':'60'}) 
    writer.writerow({'姓名': 'Peter', '年龄': '10', '身高': '181cm', '体重':'80'})
    writer.writerow({'姓名': 'James', '年龄': '14', '身高': '180cm', '体重':'90'})
    writer.writerow({'姓名': 'Jhons', '年龄': '15', '身高': '196cm', '体重':'100'})



# 操作csv文件

import pandas

uponup = pandas.read_csv('./python爬虫/uponup.csv')
print(uponup)

import pandas as pd

b = ['Peter', 'Paul', 'Curry']
c = ['18岁', '19岁', '20岁']
d = ['180cm', '174cm', '169cm']
e = ['120', '110', '90']

df = pd.DataFrame({'姓名' : b, '年龄' : c, '身高' : d, '体重': e})
df.to_csv('./python爬虫/uponup.csv', index=False, sep=',')
