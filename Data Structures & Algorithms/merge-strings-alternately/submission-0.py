class Solution:
    def mergeAlternately(self, s1: str, s2: str) -> str:
        len1, len2 = len(s1), len(s2)
        l1, l2 = 0, 0
        res = ""
        while l1< len1 and l2 <len2:
            res += s1[l1] + s2[l2]
            l1 +=1
            l2 +=1

        while l1< len1:
            res += s1[l1]
            l1 += 1
        while l2 < len2:
            res += s2[l2]
            l2 += 1
        return res