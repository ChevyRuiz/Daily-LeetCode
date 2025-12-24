import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        ans = R

        while L <= R:
            k = (L  + R) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                ans = min(ans, k)
                R = k - 1
            else:
                L = k + 1
        return ans
