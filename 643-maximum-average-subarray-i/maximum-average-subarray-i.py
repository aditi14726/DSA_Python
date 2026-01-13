class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        curr_sum=0
        max_avg=float('-inf')
        for right in range(len(nums)):  
            curr_sum+=nums[right]
            
            if right-left+1 == k:
                max_avg= max(max_avg, curr_sum/(right-left+1))
                curr_sum-= nums[left]
                left+=1
        return max_avg