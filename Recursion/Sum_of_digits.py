def sum_of_digits(n):
    if n < 10:
        return n  # if its single number then print as it is
    else:
        # if its multiple numbers then sum all the numbers
        return n % 10 + sum_of_digits(n / 10)


a = int(input("Enter the numbers"))
print(sum_of_digits(a))
