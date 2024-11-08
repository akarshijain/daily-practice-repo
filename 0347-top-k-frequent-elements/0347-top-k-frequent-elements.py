class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1, 2, 2, 3, 3, 3, 4] k = 2

        nums_count_map = {}
        for num in nums:
            if num in nums_count_map:
                nums_count_map[num] += 1
            else:
                nums_count_map[num] = 1

        count = defaultdict(list)
        for num in nums_count_map:
            count[nums_count_map[num]].append(num)
        
        result = []
        for i in range(len(nums), -1, -1):
            if k == 0:
                return result

            if count[i] == []:
                continue
            else:
                for c in count[i]:
                    if k == 0:
                        return result
                    result.append(c)
                    k -= 1

        return result
        


        