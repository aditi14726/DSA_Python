class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []
        pCount = [0] * 26
        window = [0] * 26

        for ch in p:
            pCount[ord(ch) - ord('a')] += 1

        left = 0
        for right in range(len(s)):
            window[ord(s[right]) - ord('a')] += 1

            if right - left + 1 > len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1

            if window == pCount:
                res.append(left)

        return res
