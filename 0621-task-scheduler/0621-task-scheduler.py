class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = {}
        for task in tasks:
            if task not in task_count:
                task_count[task] = 0
            task_count[task] += 1

        task_heap = []
        heapq.heapify(task_heap)
        for task in task_count:
            heapq.heappush(task_heap, -1 * task_count[task])

        task_q = deque()
        idle_time_required = n
        processing_time = 0

        while task_heap or task_q:
            processing_time += 1

            if not task_heap:
                processing_time = task_q[0][0]
            else:
                num_task_left = (-1 * heapq.heappop(task_heap)) - 1
                if num_task_left != 0:
                    next_proceesing_time = processing_time + idle_time_required
                    task_q.append((next_proceesing_time, num_task_left))

            if task_q and task_q[0][0] == processing_time:
                _, next_task = task_q.popleft()
                heapq.heappush(task_heap, -1 * next_task)

        return processing_time

        