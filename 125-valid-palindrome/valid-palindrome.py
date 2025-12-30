class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        left=0
        s = s.lower()
        for ch in s:
            if ch.isalnum():
                new+=ch
        right= len(new)-1
        while (left < right):
            if (new[left] != new[right]):
                 return False
            left+=1
            right-=1
        return True

        #rev=new[::-1]
        #if rev==new:
         #   return True
        #else:
         #   return False