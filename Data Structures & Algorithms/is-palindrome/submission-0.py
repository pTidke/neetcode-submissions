class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = [ch.lower() for ch in s if ch.isalnum()]
        xstrp = list(reversed(stripped))
        return stripped == xstrp