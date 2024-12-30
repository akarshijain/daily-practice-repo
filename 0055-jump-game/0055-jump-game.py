class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canJump = [False] * len(nums)
        canJump[-1] = True

        for index in range(len(nums) - 2, -1, -1):
            max_jump = nums[index]
            for jump in range(1, max_jump + 1):
                if canJump[index + jump]:
                    canJump[index] = True
                    break

        return canJump[0]
