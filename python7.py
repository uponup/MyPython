
lines = open('token.txt', 'r')


vars = [ line.split(',')[1] for line in lines ]
vars.sort()
print(vars)



set_vars = set(vars)

if len(set_vars) == len(vars) :
    print("没有重复数据")
else:
    print('有重复数据')