def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


a = int(input("Enter the number: "))
print(fibo(a))
