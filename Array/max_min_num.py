def min_max(arr):
    for i in arr:
        a = max(arr)
        b = min(arr)
    return f"Maximum is {a}\nMinimum is {b}"


a = list(map(int, input("Enter the numbers: ").split(" ")))
print(min_max(a))
