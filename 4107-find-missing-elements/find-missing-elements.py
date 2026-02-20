class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
       # s=set(nums)
        start=min(nums)
        end=max(nums)
        missing=[]
        for x in range(start,end+1):
            if x not in nums:
                missing.append(x)
        return missing
