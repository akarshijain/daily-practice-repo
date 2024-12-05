class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}

        for i in range(len(points)):
            adj[i] = []

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                man_distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((man_distance, j))
                adj[j].append((man_distance, i))

        visited = set()
        visited.add(0)

        min_heap = [(0, 0)]
        heapq.heapify(min_heap)
        for dist, nei in adj[0]:
            heapq.heappush(min_heap, (dist, nei))

        min_cost = 0

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            min_cost += dist
            visited.add(node)

            for dist, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (dist, nei))


        return min_cost

