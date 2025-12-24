class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for i in (sentences):
            d=i.split()
            l=len(d)
            if(l>m):
                m=l
        return m