def fibonacci(n):
    a, b, counter = 0, 1, 0
    while counter < n:
        print(b)
        a, b = b, a+b
        counter += 1

fibonacci(10)

