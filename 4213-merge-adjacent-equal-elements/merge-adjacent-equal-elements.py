class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                val = stack.pop()
                stack[-1] += val
        
        return stack