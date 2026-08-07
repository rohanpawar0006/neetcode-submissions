class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for current, prerequest in prerequisites:
            preMap[current].append(prerequest)
        visiting = set()
        def dfs(current):
            if current in visiting:
                return False
            if preMap[current] == []:
                return True
            visiting.add(current)
            for prerequest in preMap[current]:
                if not dfs(prerequest):
                    return False
            visiting.remove(current)
            preMap[current] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True