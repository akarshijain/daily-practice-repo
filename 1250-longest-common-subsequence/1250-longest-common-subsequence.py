class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        num_subsequence = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for row in range(len(num_subsequence) - 2, -1, -1):
            for col in range(len(num_subsequence[0]) - 2, -1, -1):
                if text1[row] == text2[col]:
                    num_subsequence[row][col] = 1 + num_subsequence[row + 1][col + 1]
                else:
                    num_subsequence[row][col] = max(num_subsequence[row + 1][col], \
                                                    num_subsequence[row][col + 1])

        return num_subsequence[0][0]