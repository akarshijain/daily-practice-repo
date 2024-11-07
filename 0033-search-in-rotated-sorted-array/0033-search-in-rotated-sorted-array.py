class Solution:
    def findPivot(self, nums):
        pivot = 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= nums[-1]:
                pivot = mid
                right = mid - 1

            else:
                left = mid + 1

        return pivot

    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        print(nums)
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return -1


    def search(self, nums: List[int], target: int) -> int:
        index = -1
        pivot = self.findPivot(nums)

        if target >= nums[pivot] and target <= nums[-1]:
            index = self.binarySearch(nums, target, pivot, len(nums) - 1)

        if index != -1:
            return index
        else:
            return self.binarySearch(nums, target, 0, pivot - 1)

        

        
        