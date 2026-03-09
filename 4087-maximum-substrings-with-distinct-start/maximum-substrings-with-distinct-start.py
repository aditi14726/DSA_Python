class Solution:
    def maxDistinct(self, s: str) -> int:
        new_s= set()
        for i in s:
                new_s.add(i)
        return len(new_s)