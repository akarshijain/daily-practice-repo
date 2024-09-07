class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        string_freq_map = {}

        for right in range(len(s)):
            if s[right] in string_freq_map:
                string_freq_map[s[right]] += 1
            else:
                string_freq_map[s[right]] = 1

            max_freq = max(max_freq, string_freq_map[s[right]])

            if (right - left + 1) - max_freq > k:
                string_freq_map[s[left]] -= 1
                left += 1

        return (right - left + 1)

        
            
