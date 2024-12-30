class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        num_jumps = 0
        while right < len(nums) - 1:
            max_jump = 0
            for index_value in range(left, right + 1):
                max_jump = max(max_jump, index_value + nums[index_value])
            num_jumps += 1
            left = right + 1
            right = max_jump

        return num_jumps