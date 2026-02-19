class Solution:
    def scoreBalance(self, s: str) -> bool:  
        total=0
        for ch in s:
            total+=ord(ch)-ord('a')+1
        left_score=0
        for i in range(len(s)-1):   
            left_score+=ord(s[i])-ord('a')+1
            if left_score == (total-left_score):
                return True
        return False        