class Solution:
    def maxDistinct(self, s: str) -> int:
        new_s=""
        for i in s:
            if i not in new_s:
                new_s+=i
        return len(new_s)