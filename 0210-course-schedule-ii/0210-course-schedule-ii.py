class Solution:
    def __init__(self):
        self.visited = set()
        self.prereq_map = {}

        self.result_set = set()
        self.result = []

    def isValid(self, course):
        if course in self.visited:
            return False

        if self.prereq_map[course] == []:
            if course not in self.result_set:
                self.result_set.add(course)
                self.result.append(course)
            return True

        self.visited.add(course)

        for prereq in self.prereq_map[course]:
            if not self.isValid(prereq):
                return False
        
        if course not in self.result_set:
            self.result_set.add(course)
            self.result.append(course)
        self.prereq_map[course] = []
        self.visited.remove(course)

        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]

            if course not in self.prereq_map:
                self.prereq_map[course] = []

            if prereq not in self.prereq_map:
                self.prereq_map[prereq] = []

            self.prereq_map[course].append(prereq)

        for i in range(numCourses):
            if i not in self.prereq_map:
                self.prereq_map[i] = []

        for course in self.prereq_map:
            if not self.isValid(course):
                return []

        return self.result