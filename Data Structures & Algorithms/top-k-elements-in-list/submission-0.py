from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)
        for x in nums:
            a[x] += 1
        a = dict(sorted(a.items(), key= lambda item : item[1], reverse=True))
        print(list(a.keys())[:k])
        return list(a.keys())[:k]