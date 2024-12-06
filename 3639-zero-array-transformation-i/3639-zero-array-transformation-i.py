class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        query_dec = []

        for i in range(len(nums) + 1):
            query_dec.append(0)

        for start, end in queries:
            query_dec[start] += 1
            query_dec[end + 1] -= 1 

        for i in range(1, len(query_dec)):
            query_dec[i] += query_dec[i - 1]

        
        for i, num in enumerate(nums):
            if num > query_dec[i]:
                return False
  
        return True