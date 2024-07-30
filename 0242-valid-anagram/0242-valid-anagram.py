class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map = {}

        for char in s:
            if char not in anagram_map:
                anagram_map[char] = 1
            else:
                anagram_map[char] += 1

        for char in t:
            if char not in anagram_map:
                return False
            else:
                anagram_map[char] -= 1

        for char in anagram_map:
            if anagram_map[char] != 0:
                return False

        return True