class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        ls = ''
        mlen = 0
        for c in s:
            if c not in ls:
                ls += c
            else :
                ls = ls[ls.index(c) + 1 :] + c
            mlen = max(mlen, len(ls))

        return mlen