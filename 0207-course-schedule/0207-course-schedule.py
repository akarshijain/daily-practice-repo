class Solution:
    def __init__(self):
        self.visited = set()
        self.prereq_map = {}

    def isValid(self, course):
        if course in self.visited:
            return False

        if self.prereq_map[course] == []:
            return True

        self.visited.add(course)

        for prereq in self.prereq_map[course]:
            if not self.isValid(prereq):
                return False
            
        self.prereq_map[course] = []
        self.visited.remove(course)

        return True
            

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]

            if course not in self.prereq_map:
                self.prereq_map[course] = []

            if prereq not in self.prereq_map:
                self.prereq_map[prereq] = []

            self.prereq_map[course].append(prereq)

        for course in self.prereq_map:
            if not self.isValid(course):
                return False

        return True