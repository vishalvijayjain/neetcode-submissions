class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        arr = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            arr[value].append(key)
        
        res = []
        for i in range(len(arr)-1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
