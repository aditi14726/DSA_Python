class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left=0
        window_product=1
        count=0
        if k<=1:
            return 0
        for right in range(len(nums)):  
            window_product*=nums[right]
            while window_product >= k:
                window_product//=nums[left]
                left+=1
            count+=right-left+1
        return count