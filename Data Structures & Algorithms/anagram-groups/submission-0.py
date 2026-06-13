class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for a in strs:
            m = ''.join(sorted(a))
            if m not in x.keys():
                x[m] = [a]
            else:
                x[m].append(a)
        
        return (list(x.values()))