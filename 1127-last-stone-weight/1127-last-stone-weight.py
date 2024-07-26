class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            heapq._heapify_max(stones)

            num_1 = heapq._heappop_max(stones)
            num_2 = heapq._heappop_max(stones)

            if num_1 != num_2:
                heapq.heappush(stones, abs(num_2 - num_1))

        if len(stones) == 0:
            return 0

        if len(stones) == 1:
            return stones[0]
        