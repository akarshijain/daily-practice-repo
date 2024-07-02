class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = collections.deque(students)
        num_hungry = 0

        while students_queue and num_hungry != len(students_queue):
            if students_queue[0] == sandwiches[0]:
                num_hungry = 0
                sandwiches.pop(0)
            else:
                students_queue.append(students_queue[0])
                num_hungry += 1

            students_queue.popleft()
        
        return len(students_queue)