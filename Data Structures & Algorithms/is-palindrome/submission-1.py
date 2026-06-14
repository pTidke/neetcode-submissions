class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''.join([ch.lower() for ch in s if ch.isalnum()])
        return stripped == stripped[::-1]