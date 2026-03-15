def smallest(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


arr = [45, 87, 56, 23, 54]
print("Smallest num in array is:", smallest(arr))
