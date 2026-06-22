class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1 = {}
        freq_2 = {}

        for char in s:
            if char in freq_1:
                freq_1[char] += 1
            else:
                freq_1[char] = 1

        for char in t:
            if char in freq_2:
                freq_2[char] += 1
            else:
                freq_2[char] = 1

        if freq_1 == freq_2:
            return True
        return False
        