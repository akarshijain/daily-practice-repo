class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for index, num in enumerate(nums):
            difference = target - num

            if difference in index_map:
                return [index_map[difference], index]
            
            index_map[num] = index

            