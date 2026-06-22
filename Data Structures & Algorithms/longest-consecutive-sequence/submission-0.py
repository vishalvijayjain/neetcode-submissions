class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for s in numSet:
            if s-1 not in numSet:
                length = 0
                while (s + length) in numSet:
                    length +=1
                longest = max(longest, length)
        return longest