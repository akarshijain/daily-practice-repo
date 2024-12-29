class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()

        neighbours_map = {}
        for i in range(1, n+1):
            neighbours_map[i] = []

        for src, dst, wt in times:
            neighbours_map[src].append((dst, wt))

        signal_map = {}
        min_heap = [(0, k)]
        max_delay = -1
        while min_heap:
            wt, src = heapq.heappop(min_heap)
            if src in signal_map:
                continue

            signal_map[src] = wt
            max_delay = max(max_delay, wt)
            visited.add(src)

            for nei, nei_wt in neighbours_map[src]:
                heapq.heappush(min_heap, (wt + nei_wt, nei))
        
        return max_delay if len(visited) == n else -1