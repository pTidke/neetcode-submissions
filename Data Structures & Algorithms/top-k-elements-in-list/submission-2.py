from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        m = [[] for _ in range(len(nums) + 1)]
        # print(m)

        for x, y in counts.items():
            m[y].append(x)
        
        ans = []
        for i in range(len(m)-1, 0, -1):
            for num in m[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
