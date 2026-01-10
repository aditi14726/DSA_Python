class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr_sum=0
        store={0:-1}
        #i=-1
        for i,num in enumerate (nums): 
            curr_sum+=num
           # i+=1
            if k != 0:
                rem = curr_sum % k
            else:
                rem = curr_sum

            if rem in store:
                if i - store[rem] >=2:
                  return True
            else:
                store[rem]=i
        return False
