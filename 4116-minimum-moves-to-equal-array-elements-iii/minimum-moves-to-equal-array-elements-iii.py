class Solution:
    def minMoves(self, nums: List[int]) -> int: 
        k=max(nums)
        total=0
        for i in range(len(nums)):
            total+=(k-nums[i])
        return total  