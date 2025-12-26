class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]: 
        unique_set = set()      # 👈 list ki jagah set
        duplicates = []
        i = 0

        while i < len(nums):
            if nums[i] not in unique_set:
                unique_set.add(nums[i])
                i += 1
            else:
                duplicates.append(nums[i])
                nums.pop(i)

        return duplicates