from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        s = set(nums)
        avg = sum(nums) / len(nums)
        k = max(1,int(avg) + 1)
        while True:
            if k not in s:
                return k
            k += 1