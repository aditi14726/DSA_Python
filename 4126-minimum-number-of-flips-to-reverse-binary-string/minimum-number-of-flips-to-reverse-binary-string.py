class Solution:
    def minimumFlips(self, n: int) -> int:
        res = ""
        count=0
        while n > 0:
            res = str(n % 2) + res
            n //= 2
        rev=res[::-1]
        for i in range(len(res)):
            if rev[i] != res[i]:
                count+=1
        return count
