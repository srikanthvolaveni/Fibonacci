def fibonacci(n):
    a=0
    b=1

    print(a)
    print(b)
    for i in range(3,n+1):

        c = a+b 
        a = b 
        b = c

        print(c)


num = int(input("enter the number: "))
fibonacci(num)