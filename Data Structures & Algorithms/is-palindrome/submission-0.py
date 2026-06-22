class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char
        left = 0
        right = len(newS) - 1

        while left < right:
            if newS[left].lower() != newS[right].lower():
                return False
            left +=1
            right -=1
        return True
