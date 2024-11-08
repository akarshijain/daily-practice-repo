class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_map = {}

        for char in s:
            if char in word_map:
                word_map[char] += 1

            else:
                word_map[char] = 1

        for char in t:
            if char in word_map:
                word_map[char] -= 1

            else:
                return False

        for char in word_map:
            if word_map[char] != 0:
                return False

        return True

        