class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_map = {}
        result = []

        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1

        arr = [[] for i in range(len(nums) + 1)]

        for key in num_map:
            count = num_map[key]
            arr[count-1].append(key)

        for nums in arr[::-1]:
            for num in nums:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
