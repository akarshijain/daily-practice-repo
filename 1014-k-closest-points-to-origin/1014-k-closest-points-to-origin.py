class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        index = 0
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            heapq.heappush(min_heap, (distance, index))
            index += 1

        k_closest_points = []
        while k > 0:
            _, index = heapq.heappop(min_heap)
            k_closest_points.append(points[index])
            k -= 1

        return k_closest_points