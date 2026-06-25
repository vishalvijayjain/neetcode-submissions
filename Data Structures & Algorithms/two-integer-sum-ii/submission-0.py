class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l, r = 0, len(num) -1
        while num[l] + num[r] != target:
            while num[l] + num[r] > target and r > l:
                r-=1
            while num[l] + num[r]< target and l < r:    
                l+=1
        return [l+1, r+1]