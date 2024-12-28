class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index_map = {}
        for index in range(len(nums)):
            index_map[index] = nums[index]

        nums.sort()

        is_smaller_count_map = {}
        is_smaller_count_map[nums[0]] = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] > nums[i - 1]:
                is_smaller_count_map[nums[i]] = i

        answer = []
        for i in range(len(nums)):
            answer.append(is_smaller_count_map[index_map[i]])

        return answer
