class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_char_count = {}
        for char in s:
            if char not in s_char_count:
                s_char_count[char] = 0
            s_char_count[char] += 1

        for char in t:
            if char not in s_char_count:
                return char
            s_char_count[char] -= 1

        for char in s_char_count:
            if s_char_count[char] < 0:
                return char
            

