class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        ans = [1] * (len(nums))
        for i, n in enumerate(nums):
            ans[i] = prefix
            prefix *= n
        
        postfix = 1
        for i, n in enumerate(nums[::-1]):
            print(len(nums) - 1 - i)
            ans[len(nums) - 1 - i] *= postfix
            postfix *= n
        
        return ans
        