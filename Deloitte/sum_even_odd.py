def sum(s):
    even = 0
    odd = 0
    for i in range(len(s)):
        if i % 2 == 0:  # check the index is divisible
            even += s[i]  # if remainder is zero then sum its value
        else:
            odd += s[i]
    return even, odd


arr = [1, 2, 3, 4, 5, 6]
even, odd = sum(arr)
print(f"Even index positions sum {even}\nOdd index positions sum {odd}")
