class Solution:
    def maxScore(self, s: str) -> int:
        max_split_score = 0
        for split_index in range(len(s) - 1):
            str1 = s[0:split_index + 1]
            str2 = s[split_index + 1:len(s)]

            count_zero, count_one = 0, 0
            for num in str1:
                if num == "0":
                    count_zero += 1

            for num in str2:
                if num == "1":
                    count_one += 1

            max_split_score = max(max_split_score, count_zero + count_one)

        return max_split_score
            