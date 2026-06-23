class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_zero, pro = 0, 1

        for num in nums:
            if num:
                pro *= num
            else:
                cnt_zero += 1
        
        if cnt_zero > 1: return [0]* len(nums)

        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if cnt_zero:
                if not num:
                    res[i] = pro
            else:
                res[i] = pro // num
        return res
                