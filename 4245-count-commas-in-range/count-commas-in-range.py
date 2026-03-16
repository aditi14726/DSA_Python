class Solution:
    def countCommas(self, n: int) -> int:
        commas=0
        for i in range(1,n+1):
            digits=len(str(i))
            commas+=(digits-1)//3
        return commas

        