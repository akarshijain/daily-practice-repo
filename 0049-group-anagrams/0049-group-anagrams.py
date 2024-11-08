class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1

            # anagram_key = ''.join(str(k) for k in key) # Always use tuple for 
                                                         # dict keys because they 
                                                         # are hashable and immutable. 
                                                         # List cannot be used. 
                                                         # Here 10 is being treated 
                                                         # as 1 and 0 producing the same 
                                                         # key for ["bdddddddddd","bbbbbbbbbbc"].
            anagram_key = tuple(key)
            
            if anagram_key not in anagram_map:
                anagram_map[anagram_key] = []

            anagram_map[anagram_key].append(word)

        return list(anagram_map.values())
