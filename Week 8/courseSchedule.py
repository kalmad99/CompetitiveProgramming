class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        visited = set()
        courses = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            courses[crs].append(pre)

        for crs in range(numCourses):
            if self.dfs(courses, crs, visited) == False:
                return False
        return True

    def dfs(self, courses, course, visited):
        if course in visited:
            return False

        if courses[course] == []:
            return True

        visited.add(course)
        for pre in courses[course]:
            if self.dfs(courses, pre, visited) == False:
                return False
        visited.remove(course)
        courses[course] = []
        return True

