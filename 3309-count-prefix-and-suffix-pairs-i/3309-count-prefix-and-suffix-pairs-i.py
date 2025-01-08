class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        return str1 == str2[:len(str1)] == str2[len(str2) - len(str1):]

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                str1, str2 = words[i], words[j]
                if self.isPrefixAndSuffix(str1, str2):
                    count += 1

        return count
