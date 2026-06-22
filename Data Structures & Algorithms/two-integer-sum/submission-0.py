class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {int:int}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in index:
                return [index[j],i]
            index[nums[i]] = i
        return []