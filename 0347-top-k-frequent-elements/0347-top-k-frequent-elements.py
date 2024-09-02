class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}
        result = []
        max_times = len(nums)

        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        while k != 0:
            for key in count_map:
                if count_map[key] == max_times:
                    result.append(key)
                    k -= 1
                    
            max_times -= 1
        
        return result
