class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = f"{x}"
        #s=str(x)   This and above way....both are correct
        left=0
        right=len(s)-1
        while (left<right):
            if s[left]!=s[right]: 
                return False
            left+=1
            right-=1
        return True