def freq(s):
    count = {}
    for i in s:
        count[i] = count.get(i, 0) + 1
    return count


arr = [10, 5, 10, 15, 10, 5]
print(freq(arr))

# Time: O(n)
# Space: O(n)
