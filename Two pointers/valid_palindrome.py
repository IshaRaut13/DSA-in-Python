import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return a == a[::-1]