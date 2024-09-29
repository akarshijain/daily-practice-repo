class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = -1

        for i in range(len(nums)+1):
            if i not in nums:
                num = i

        return num