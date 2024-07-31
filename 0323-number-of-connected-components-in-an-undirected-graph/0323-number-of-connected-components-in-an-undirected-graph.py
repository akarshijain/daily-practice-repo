class Solution:
    def __init__(self):
        self.visit = set()
        self.adjList = {}
        self.count = 0

    def dfs(self, node) -> int:
        if node in self.visit:
            return

        self.visit.add(node)

        if self.adjList[node] == []:
            return

        for nei in self.adjList[node]:
            self.dfs(nei)


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        for node, nei in edges:
            if node not in self.adjList:
                self.adjList[node] = []
            if nei not in self.adjList:
                self.adjList[nei] = []

            self.adjList[node].append(nei)
            self.adjList[nei].append(node)

        for i in range(n):
            if i not in self.adjList:
                self.adjList[i] = []

        print(self.adjList)

        for node in self.adjList:
            if node not in self.visit:
                self.dfs(node)
                self.count += 1

        return self.count
