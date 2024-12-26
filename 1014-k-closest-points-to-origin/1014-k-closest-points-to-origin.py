class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        for index, (x, y) in enumerate(points):
            euc_distance = sqrt((x * x) + (y * y))
            heapq.heappush(min_heap, (euc_distance, index))
        
        result = []
        while k > 0:
            _, index = heapq.heappop(min_heap)
            result.append(points[index])
            k -= 1

        return result
        