arr = [1, 3, 8, 5, 0, 2]
target = 6
l, r, sum, maxlen = 0, 0, 0, 0
while r < len(arr):
    sum = sum + arr[r]

    # l is shrinking is sum is greater than target
    if sum > target:
        sum = sum - arr[l]
        l += 1

    #  r is expanding till we achieve target
    if sum <= target:
        maxlen = max(maxlen, r - l + 1)
    r += 1

print("Max window size is:", maxlen)
