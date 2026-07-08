class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        count = set()
        l, r = 0, 0
        if not s:
            return 0
        while r < len(s):
            if s[r] not in count:
                count.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                res = max(res, r - l)
                while s[r] in count:
                    count.remove(s[l])
                    l += 1
        return res
