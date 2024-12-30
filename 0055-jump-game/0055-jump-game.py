class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_position = len(nums) - 1

        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= final_position:
                final_position = index

        return final_position == 0
