def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        return a
    elif n == 2 :
        return (a, b)
    else:
        print(a, b, end = ", ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b, end = ", ")
        

n = int(input("enter num  "))
print(fibonacci(n))            