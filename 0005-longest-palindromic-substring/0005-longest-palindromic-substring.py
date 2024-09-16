class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ""

        for i in range(len(s)):
            left = i
            right = i
            while min(left, right) >= 0 and max(left, right) < len(s) and s[left] == s[right]:
                if right - left + 1 > len(max_str):
                    max_str = s[left:right + 1]
                left -= 1
                right += 1

            left = i
            right = i + 1
            while min(left, right) >= 0 and max(left, right) < len(s) and s[left] == s[right]:
                if right - left + 1 > len(max_str):
                    max_str = s[left:right + 1]
                left -= 1
                right += 1

        return max_str


            