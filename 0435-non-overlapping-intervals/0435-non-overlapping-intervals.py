class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_heap = []
        heapq.heapify(min_heap)

        for interval in intervals:
            heapq.heappush(min_heap, interval)

        non_overlap_intervals = [heapq.heappop(min_heap)]

        while min_heap:
            start, end = heapq.heappop(min_heap)
            if start < non_overlap_intervals[-1][1]:
                if end < non_overlap_intervals[-1][1]:
                    non_overlap_intervals[-1][1] = end
            else:
                non_overlap_intervals.append([start, end])

        return len(intervals) - len(non_overlap_intervals)