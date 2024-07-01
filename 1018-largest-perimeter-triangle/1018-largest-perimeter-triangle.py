class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        perimeter = 0
        nums.sort(reverse = True)
        index = 2

        while index < len(nums):
            if nums[index] + nums[index - 1] > nums[index - 2]:
                perimeter = max(perimeter, nums[index] + nums[index - 1] + nums[index - 2])
            index += 1

        return perimeter
        