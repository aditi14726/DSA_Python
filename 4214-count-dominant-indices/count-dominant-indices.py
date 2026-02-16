class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        right_sum = 0
        right_count = 0
        result = 0

        # traverse from right to left
        for num in reversed(nums):
            if right_count > 0 and num * right_count > right_sum:
                result += 1

            right_sum += num
            right_count += 1

        return result
