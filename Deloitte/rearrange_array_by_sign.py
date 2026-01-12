def rearrange(s):
    # It creates a new list of the same size as nums, filled with zeros.
    res = [0] * len(s)
    l = 0  # positive integer
    r = 1  # negative integer
    for i in s:
        if i > 0:
            res[l] = i
            l += 2
        else:
            res[r] = i
            r += 2
    return res


s = [3, 1, -2, -5, 2, -4]
print(rearrange(s))
