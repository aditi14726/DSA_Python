class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def can(k):
            ops=0
            for x in nums: 
                ops += (x + k - 1) // k # ceil(x / k) 
            return ops <= k * k
        low,high=1,1
        while not can(high):
            high *= 2
        while (low <= high):
            mid=(high+low) // 2
            if can(mid):
                high=mid-1
            else:
                low=mid+1
        return low