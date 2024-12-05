class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {}

        for i in range(1, n + 1):
            adj_list[i] = []

        for u, v, w in times:
            adj_list[u].append((v, w))

        min_time = {}
        max_delay = -1
        min_heap = [(0, k)]
        heapq.heapify(min_heap)

        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if node in min_time:
                continue

            min_time[node] = weight
            max_delay = max(max_delay, weight)

            for nei, wei in adj_list[node]:
                if nei not in min_time:
                    heapq.heappush(min_heap, (weight + wei, nei))

        if len(min_time) != len(adj_list):
            return -1
            
        return max_delay
            

