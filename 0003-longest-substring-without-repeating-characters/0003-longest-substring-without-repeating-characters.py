class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        string_set = set()

        for right in range(len(s)):
            if s[right] in string_set:
                while s[right] in string_set:
                    string_set.remove(s[left])
                    left += 1
            string_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len