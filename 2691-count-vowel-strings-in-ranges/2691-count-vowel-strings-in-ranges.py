class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = "aeiou"
        vowel_words = [0] * len(words)
        if words[0][0] in vowels and words[0][-1] in vowels:
            vowel_words[0] = 1

        index = 1
        for word in words[1:]:
            vowel_words[index] = vowel_words[index - 1]
            if word[0] in vowels and word[-1] in vowels:
                vowel_words[index] += 1
            index += 1

        ans = []
        for start, end in queries:
            range_count = vowel_words[end] - vowel_words[start]
            if words[start][0] in vowels and words[start][-1] in vowels:
                range_count += 1
            ans.append(range_count)

        return ans