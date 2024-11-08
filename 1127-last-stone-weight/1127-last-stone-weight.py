class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        heapq.heapify(max_heap)

        for stone in stones:
            heapq.heappush(max_heap, -1 * stone)

        while len(max_heap) > 1 :
            
            y = -1 * heapq.heappop(max_heap)
            x = -1 * heapq.heappop(max_heap)

            if x != y:
                y = y - x
                heapq.heappush(max_heap, -1 * y)
            else:
                heapq.heappush(max_heap, 0)

        return -1 * max_heap[0]