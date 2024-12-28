class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        index = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                index += 1

        if index == len(nums) - 1:
            return True

        index = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                index += 1

        if index == len(nums) - 1:
            return True

        return False