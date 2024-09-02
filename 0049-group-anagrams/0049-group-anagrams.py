class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_map = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = []
                anagram_map[key].append(word)

        for key in anagram_map:
            result.append(anagram_map[key])

        return result

        