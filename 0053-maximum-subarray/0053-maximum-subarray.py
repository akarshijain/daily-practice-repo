class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr_sum = [0] * len(nums)

        max_sum = arr_sum[0] = nums[0]
        
        for index in range(1, len(nums)):
            if nums[index] > nums[index] + arr_sum[index - 1]:
                arr_sum[index] = nums[index]
            else:
                arr_sum[index] = nums[index] + arr_sum[index - 1]

            max_sum = max(max_sum, arr_sum[index])

        return max_sum