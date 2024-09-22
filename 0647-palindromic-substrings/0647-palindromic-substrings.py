class Solution:
    def countSubstrings(self, s: str) -> int:
        num_palindrome = 0

        for i in range(len(s)):
            left = i
            right = i

            while min(left, right) >= 0 and max(left, right) < len(s) and s[left] == s[right]:
                num_palindrome += 1
                left -= 1
                right += 1

            left = i
            right = i + 1
            while min(left, right) >= 0 and max(left, right) < len(s) and s[left] == s[right]:
                num_palindrome += 1
                left -= 1
                right += 1
        return num_palindrome