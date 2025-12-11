def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * power(a, n - 1)


a = int(input("Enter the base number: "))
n = int(input("Enter the power number: "))
print("Answer: ", power(a, n))


# Enter the base number: 4
# Enter the power number: 2
# Answer:  16
