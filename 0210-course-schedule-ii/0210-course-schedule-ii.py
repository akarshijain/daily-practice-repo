class Solution:
    def __init__(self):
        self.prereq_for_course = {}
        self.order_of_courses = []
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
            else:
                if prereq not in self.order_of_courses:
                    self.order_of_courses.append(prereq)

        self.prereq_for_course[course] = []
        self.visit.remove(course)

        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        for course, prereq in prerequisites:
            if course not in self.prereq_for_course:
                self.prereq_for_course[course] = []
            if prereq not in self.prereq_for_course:
                self.prereq_for_course[prereq] = []

            self.prereq_for_course[course].append(prereq)

        for i in range(numCourses):
            if i not in self.prereq_for_course:
                self.prereq_for_course[i] = []

        for course in self.prereq_for_course:
            if not self.dfs(course):
                return []
            else:
                if course not in self.order_of_courses:
                    self.order_of_courses.append(course)

        return self.order_of_courses
