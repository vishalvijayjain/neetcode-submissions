class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        count_sorted = dict(sorted(count.items(), key=lambda item:item[1], reverse =True))
        res = []
        for i, (key,value) in enumerate(count_sorted.items()):
            if i== k:
                break
            res.append(key)
        return res
