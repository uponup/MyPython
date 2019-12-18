def fibo(n):
    a, b, counter = 0, 1, 0
    while counter < n:
        print(b, end=' ')
        a, b = b, a + b
        counter += 1
        

def fibo2(n):
    result = []
    a, b, counter = 0, 1, 0
    while counter < n:
        result.append(b)
        a, b = b, a+b
        counter += 1
    print(result)
    return result
