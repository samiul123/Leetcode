import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(rate_per_hour):
            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile / rate_per_hour)
            return total_hour <= h

        low, high = 1, max(piles)
        k = 1

        while low <= high:
            mid = (low + high) // 2

            if can_eat(mid):
                k = mid
                high = mid - 1
            else:
                low = mid + 1

        return k
