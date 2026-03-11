class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        b = bin(n)[2:]   
        flip = ""
        
        for i in b:
            if i == "1":
                flip += "0"
            else:
                flip += "1"
        
        return int(flip, 2)