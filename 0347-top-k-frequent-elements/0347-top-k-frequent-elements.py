class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count_map = {}
        for num in nums:
            if num not in num_count_map:
                num_count_map[num] = 0
            num_count_map[num] += 1

        num_count_arr = [[] for _ in range(len(nums))]
        for num in num_count_map:
            num_count_arr[num_count_map[num] - 1].append(num)
        
        result = []
        for count in num_count_arr[-1::-1]:
            if not count:
                continue

            for num in count:
                result.append(num)

        return result[:k]