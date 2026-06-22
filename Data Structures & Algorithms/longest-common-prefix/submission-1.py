class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c = strs[0]
        k = ""
        for i in range(len(c)):
            char = c[i]
            for s in strs:
                if i >= len(s) or char != s[i]:
                    return k
            k += char
        return k