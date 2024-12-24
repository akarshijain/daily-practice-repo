class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        heapq.heapify(min_heap)

        for stone_weight in stones:
            heapq.heappush(min_heap, -1 * stone_weight)

        while len(min_heap) > 1:
            y = -1 * heapq.heappop(min_heap)
            x = -1 * heapq.heappop(min_heap)
            if x == y:
                heapq.heappush(min_heap, 0)
            if x != y:
                heapq.heappush(min_heap, x - y)

        return -1 * min_heap[0]
        