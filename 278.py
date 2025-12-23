class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n
        while L <= R:
            M = (L + R) // 2
            if isBadVersion(M) and isBadVersion(M - 1):
                R = M - 1
            elif not isBadVersion(M):
                L = M + 1
            else:
                return M
