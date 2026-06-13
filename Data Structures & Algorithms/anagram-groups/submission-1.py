from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for a in strs:
            ct = [0] * 26
            for i in a:
                ct[ord(i) - ord('a')] += 1
            x[tuple(ct)].append(a)
        return list(x.values())
