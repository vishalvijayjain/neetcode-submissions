class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        flag = {}
        prod = 1
        zero = False
        for i, num in enumerate(nums):
            if num != 0:
                prod *= num
                flag[i] = False
            else:
                flag[i] = True
                if zero: # More than one zero
                    prod = 0
                zero = True
                continue
        res = []
        for i, num in enumerate(nums):
            if not flag[i] and zero == False:
                res.append(prod // num)
            elif not flag[i] and zero:
                res.append(0)
            else:
                res.append(prod)
        return res