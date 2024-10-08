class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:    
            mid = (left + right) // 2

            if nums[mid] <= nums[-1]:
                result = nums[mid]
                right = mid - 1
            else:
                left = mid + 1

        return result