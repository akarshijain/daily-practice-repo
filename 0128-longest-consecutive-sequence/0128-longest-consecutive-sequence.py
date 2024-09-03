class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set()

        for num in nums:
            num_set.add(num)


        sequence = 0
        longest_sequence = 0
        
        for n in num_set:
            if n-1 not in num_set:
                sequence = 1
                while(n + sequence) in num_set:
                    sequence += 1
            longest_sequence = max(longest_sequence, sequence)

        return longest_sequence