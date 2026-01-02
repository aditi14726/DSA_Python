class Solution:
    def maxArea(self, height: List[int]) -> int: 
        left=0
        right=len(height)-1
        d=0
        curr=0
        while left<right:
            if height[left] < height[right]:
                curr=height[left]* (right-left)
                d = max(d, curr)
                left+=1
            else:
                curr=height[right]* (right-left)
                d = max(d, curr)
                right-=1
        return d