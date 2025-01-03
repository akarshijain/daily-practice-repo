class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for index in range(1, len(nums)):
            prefix_sum[index] = nums[index] + prefix_sum[index - 1]

        postfix_sum = [0] * len(nums)
        postfix_sum[-2] = postfix_sum[-1] = nums[-1]
        for index in range(len(nums) - 3, -1, -1):
            postfix_sum[index] = nums[index + 1] + postfix_sum[index + 1]
        
        num_valid_splits = 0
        print(prefix_sum, postfix_sum)
        for index in range(len(nums) - 1):
            if prefix_sum[index] >= postfix_sum[index]:
                num_valid_splits += 1

        return num_valid_splits
        