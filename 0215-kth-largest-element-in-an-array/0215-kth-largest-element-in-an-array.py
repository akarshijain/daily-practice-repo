class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        heapq.heapify(max_heap)

        for num in nums:
            heapq.heappush(max_heap, -1 * num)

        # In a heap only the top element is either max or min. 
        # Heap does not sort the elements inside. 

        for i in range(k-1):
            heapq.heappop(max_heap)

        return -1 * max_heap[0]


        