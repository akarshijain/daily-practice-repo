class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        postfix = [None] * len(nums)
        result = [None] * len(nums)

        prev_val = 1
        next_val = 1
        for i in range(len(nums)):
            prefix[i] = nums[i] * prev_val
            prev_val = prefix[i]

            postfix[len(nums) - i - 1] = nums[len(nums) - i - 1] * next_val
            next_val = postfix[len(nums) - i - 1]

        print(prefix)
        print(postfix)

        result[0] = 1 * postfix[1]
        result[-1] = prefix[-2] * 1

        for i in range(1, len(result) - 1):
            result[i] = prefix[i-1] * postfix[i+1]

        return result
        