class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        
        if not word2:
            return word1

        merged_str = ""
        same_len = min(len(word1), len(word2))

        for i in range(same_len):
            merged_str += word1[i]
            merged_str += word2[i]

        if len(word1) > len(word2):
            merged_str += word1[same_len:]
        else:
            merged_str += word2[same_len:]

        return merged_str

        

