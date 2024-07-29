class Solution:
    def __init__(self):
        self.prereq_for_course = {}
        self.visit = set()

    def dfs(self, course):
        if course in self.visit:
            return False

        if not self.prereq_for_course[course]:
            return True

        self.visit.add(course)
        for prereq in self.prereq_for_course[course]:
            if not self.dfs(prereq):
                return False

        self.prereq_for_course[course] = []
        self.visit.remove(course)

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        canFinish = False

        for prereq, course in prerequisites:
            if course not in self.prereq_for_course:
                self.prereq_for_course[course] = []
            if prereq not in self.prereq_for_course:
                self.prereq_for_course[prereq] = []

            self.prereq_for_course[course].append(prereq)

        for course in self.prereq_for_course:
            if not self.dfs(course):
                return False

        return True
