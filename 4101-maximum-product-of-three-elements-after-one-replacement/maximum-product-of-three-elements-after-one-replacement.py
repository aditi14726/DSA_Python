class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        limit=100000
        nums.sort()
        n=len(nums)
        p1=nums[0]*nums[1]*nums[2]
        p2=nums[n-1]*nums[n-2]*nums[n-3]
        best_product=max(p1,p2)

        largest_p1= nums[0]*nums[1]
        largest_p2= nums[n-1]*nums[n-2]
        best_pair1= max(largest_p1,largest_p2)
        mul_limit1= best_pair1* limit

        small_p1=nums[0]*nums[n-1]
        small_p2=nums[1]*nums[n-1]
        best_pair2=min(small_p1,small_p2)
        mul_limit2= best_pair2*(-limit)

        return max(mul_limit1,mul_limit2,best_product)