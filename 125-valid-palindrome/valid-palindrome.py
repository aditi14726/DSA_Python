class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        s = s.lower()
        for ch in s:
            if ch.isalnum():
                new+=ch
        rev=new[::-1]
        if rev==new:
            return True
        else:
            return False