class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        unique_arr = []
        for num in nums:
            if num not in unique_arr:
                unique_arr.append(num)
        #for i in range(len(unique_arr)):
         #   nums[i] = unique_arr[i]
        nums[:]=unique_arr
        return len(unique_arr)




        