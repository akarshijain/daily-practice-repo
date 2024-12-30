class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1

            if tuple(key) not in anagram_map:
                anagram_map[tuple(key)] = []

            anagram_map[tuple(key)].append(word)

        return list(anagram_map.values())
            
