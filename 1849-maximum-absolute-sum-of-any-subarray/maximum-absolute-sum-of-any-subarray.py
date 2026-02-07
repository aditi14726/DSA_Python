class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_max=curr_min=(nums[0])
        max_sum=min_sum= (nums[0])
        
        for i in range(1,len(nums)):
            curr_max= max(nums[i],curr_max+nums[i])  
            curr_min= min(nums[i],curr_min+nums[i])

            max_sum=max(curr_max,max_sum)
            min_sum=min(curr_min,min_sum)
        return max(abs(max_sum), abs(min_sum))