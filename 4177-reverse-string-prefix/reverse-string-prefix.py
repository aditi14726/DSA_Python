class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        prefix = s[:k]
        reversed_prefix = prefix[::-1]
        suffix = s[k:]
        return reversed_prefix + suffix
