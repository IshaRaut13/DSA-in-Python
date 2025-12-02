class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        n = max(len(version1), len(version2))

        for i in range(n):
            r1 = int(version1[i]) if i < len(version1) else 0
            r2 = int(version2[i]) if i < len(version2) else 0

            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
        return 0


s = Solution()
print(s.compareVersion("1.0", "1.0.0"))
