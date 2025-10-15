import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        min_speed = 0

        while low <= high:
            mid = (low+high)//2

            total_hrs = 0

            for pile in piles:
                total_hrs += math.ceil(pile/mid)

    
            if total_hrs <= h :
                min_speed = mid
                high = mid -1
            else:
                low = mid + 1


        return low

        