import pymysql

# 1、连接数据库
db = pymysql.connect("localhost","root","gaojinpeng","TESTDB")

# 2、获取cursor来操作数据库
cursor = db.cursor()

# 3、创建数据表
# sql = """create table if not exists beautyGirls (
#    name char(20) not null,
#    age int)"""
# cursor.execute(sql)



# 4、插入数据
sql = """INSERT INTO beautyGirls(
         name, age)
         VALUES ('Mac', '12')"""
cursor.execute(sql)



# 5、查找数据
sql = "SELECT * FROM beautyGirls \
       WHERE name = 'Mac';"

# 执行SQL语句
cursor.execute(sql)
results = cursor.fetchall()

print(results)
for row in results:
    name = row[0]
    age = row[1]
    print(name)





# 6、删除

sql = '''
    delete from beautyGirls where name = 'Mac';
'''

cursor.execute(sql)

results = cursor.fetchall()
print(results)


# 关闭数据库
db.close()