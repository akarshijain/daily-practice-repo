class Solution:

    def __init__(self):
        self.adjList = {}
        self.visit = set()

    def dfs(self, node, prev):
        if node in self.visit:
            return False

        self.visit.add(node)

        for nei in self.adjList[node]:
            if prev == nei:
                continue

            if not self.dfs(nei, node):
                return False

        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        self.adjList = {i: [] for i in range(n)}

        for node, nei in edges:
            self.adjList[node].append(nei)
            self.adjList[nei].append(node)

        return self.dfs(0, -1) and n == len(self.visit)
