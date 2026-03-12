from typing import List

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        result = []
        i = 0
        n = len(s)

        while i < n:
            seg = ""
            j = i

            while j < n:
                seg += s[j]
                j += 1
                if seg not in seen:
                    break

            if seg in seen:   
                break

            seen.add(seg)
            result.append(seg)
            i = j

        return result