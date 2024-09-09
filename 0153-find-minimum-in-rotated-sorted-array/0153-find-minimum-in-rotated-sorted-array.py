class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                return result

            else:        
                mid = (left + right) // 2
                result = min(result, nums[left])

                if nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid

        return result