class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
       # prefix_count={0:1}
        prefix_count=[0] * k
        prefix_count[0]=1
        curr_sum=0 
        count=0
        for num in nums:
            curr_sum+=num
            rem = (curr_sum % k ) 

            count += prefix_count[rem]
            prefix_count[rem] += 1

            #if rem in prefix_count:
             #   count+=prefix_count[rem]

            #prefix_count[rem]=prefix_count.get(rem,0) +1

        return count