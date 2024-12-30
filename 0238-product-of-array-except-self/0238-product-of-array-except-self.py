class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for index in range(1, len(nums)):
            prefix[index] = prefix[index - 1] * nums[index - 1]

        postfix = [1] * len(nums)
        for index in range(len(nums) - 2, -1, -1):
            postfix[index] = postfix[index + 1] * nums[index + 1]


        result = [x * y for x, y in zip(prefix, postfix)]

        return result