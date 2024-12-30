class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest_consecutive_length = 0

        for num in nums:
            if num - 1 not in num_set:
                consecutive_length = 1

                temp = num
                while temp + 1 in num_set:
                    consecutive_length += 1
                    temp += 1

                longest_consecutive_length = max(longest_consecutive_length, consecutive_length)

        return longest_consecutive_length