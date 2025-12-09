# Compare two version strings by splitting them into revisions and comparing each revision numerically from left to right. Return -1 if the first version is smaller, 1 if it's larger, and 0 if they're equal.


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
