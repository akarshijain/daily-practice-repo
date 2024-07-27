class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0, 0]
        distance_from_origin = []
        answer = []

        for point in points:
            distance_from_origin.append((math.dist(point, origin), point[0], point[1]))
        
        heapq.heapify(distance_from_origin)

        while k:
            answer.append([distance_from_origin[0][1], distance_from_origin[0][2]])
            heapq.heappop(distance_from_origin)
            k -= 1

        return answer


        