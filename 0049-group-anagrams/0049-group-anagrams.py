class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = []
        anagram_map = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]

        for anagram in anagram_map:
            group_anagram.append(anagram_map[anagram])

        return group_anagram

        