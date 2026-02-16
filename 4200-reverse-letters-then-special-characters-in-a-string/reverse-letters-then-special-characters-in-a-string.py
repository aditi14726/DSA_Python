class Solution:
    def reverseByType(self, s: str) -> str:
# charcters aur special characters ko alg alg reverse krna h aur append bhi alg alg he  krna hai
        letters=[]
        special=[]
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                special.append(ch)
        special.reverse()
        letters.reverse()
        result=[]
        i=j=0

        for ch in s:
            if ch.isalpha():
                result.append(letters[i])
                i+=1
            else:
                result.append(special[j])
                j+=1
        return "".join(result)
