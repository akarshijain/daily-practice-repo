class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
            
        min_heap = []
        heapq.heapify(min_heap)

        for interval in intervals:
            heapq.heappush(min_heap, interval)

        merged_intervals = [heapq.heappop(min_heap)]

        while min_heap:
            start, end = heapq.heappop(min_heap)
            if start < merged_intervals[-1][1]:
                return False
            else:
                merged_intervals.append([start, end])

        return True