class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        for interval in intervals:
            heapq.heappush(min_heap, interval)

        merged_intervals = [heapq.heappop(min_heap)]

        while min_heap:
            start, end = heapq.heappop(min_heap)
            if start <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
            else:
                merged_intervals.append([start, end])

        return merged_intervals