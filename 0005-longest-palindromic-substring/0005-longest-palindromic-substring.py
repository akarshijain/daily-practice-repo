class Solution:
    def __init__(self):
        self.longest_palindrome = ""

    def isPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) \
            and s[left] == s[right]:
            tempLength = right - left + 1
            if tempLength >= len(self.longest_palindrome):
                self.longest_palindrome = s[left : right + 1]

            left -= 1
            right += 1

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            self.isPalindrome(s, i, i)
            self.isPalindrome(s, i, i+1)

        return self.longest_palindrome