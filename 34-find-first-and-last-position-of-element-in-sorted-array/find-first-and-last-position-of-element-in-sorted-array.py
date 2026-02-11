class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high= len(nums)
        while low < high:
            mid=(high+low) // 2
            if nums[mid] < target:
                low=mid+1
            else:
                high=mid
        first= low
        if first == len(nums) or nums[first] != target:
            return [-1,-1]

        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid
        last = low - 1
    
        return first, last 