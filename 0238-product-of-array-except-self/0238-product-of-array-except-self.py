class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)

        result = []

        for i in range(0, len(nums)):
            prefix[i + 1] = nums[i] * prefix[i]

        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = nums[i] * postfix[i + 1]

        for i in range(0, len(nums)):
            result.append(prefix[i] * postfix[i + 1])

        return result