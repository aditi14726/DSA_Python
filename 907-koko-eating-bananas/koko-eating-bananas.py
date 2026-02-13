class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h

        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2

            if canFinish(mid):
                high = mid - 1   # try smaller speed
            else:
                low = mid + 1    # increase speed

        return low
