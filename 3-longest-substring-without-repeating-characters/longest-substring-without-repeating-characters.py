class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        new_str=""
        max_len=0
        for right in range(len(s)):
            while s[right] in new_str:
                left+=1
                new_str=new_str[1:]
            new_str+= s[right]
            max_len = max(max_len, len(new_str))
        return max_len