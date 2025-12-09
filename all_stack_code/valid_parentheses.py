class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        match = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i == "(" or i == "{" or i == "[":
                res.append(i)
            else:
                # if nothing to pop
                if not res:
                    return False

                # if matching found and pop
                if res[-1] == match[i]:
                    res.pop()
                else:
                    return False
        return len(res) == 0


s = Solution()
input_string = s.isValid("[{()}]")
input_string1 = s.isValid("()}]")
input_string2 = s.isValid("[{]")

print(input_string)
print(input_string1)
print(input_string2)
