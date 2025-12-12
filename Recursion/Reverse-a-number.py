def reverse(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse(n // 10, rev * 10 + n % 10)


a = int(input("Enter the number: "))
print(reverse(a))
