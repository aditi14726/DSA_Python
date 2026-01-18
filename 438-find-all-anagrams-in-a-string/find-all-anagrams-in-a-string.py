from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []
        pCount = {}
        window = {}

        for ch in p:
            pCount[ch] = pCount.get(ch, 0) + 1

        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if right - left + 1 > len(p):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            if window == pCount:
                res.append(left)

        return res
