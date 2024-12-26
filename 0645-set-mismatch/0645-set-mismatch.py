class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mismatch_set = set()
        error_nums = []

        for num in nums:
            if num in mismatch_set:
                error_nums.append(num)
            mismatch_set.add(num)

        for num in range(1, len(nums) + 1):
            if num not in mismatch_set:
                error_nums.append(num)
                break

        return error_nums
            