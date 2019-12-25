def fibonacci(n):
    arr = []
    a, b, counter = 0, 1, 0
    while(counter < n):
        arr.append(b)
        a, b = b, a+b
        counter += 1

    return arr
    

def main():
    print(fibonacci(10))

if __name__ == "__main__":
    main()
