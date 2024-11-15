class Solution:
    def __init__(self):
        self.visited = set()

    def dfs(self, node, prev, adj_list):
        if node in self.visited:
            return False
            
        self.visited.add(node)

        for nei in adj_list[node]:
            if nei == prev:
                continue

            if not self.dfs(nei, node, adj_list):
                return False

        return True
            
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False

        adj_list = {}

        for i in range(n):
            adj_list[i] = []

        for node, nei in edges:
            adj_list[node].append(nei)
            adj_list[nei].append(node)

        if not self.dfs(0, -1, adj_list):
            return False

        if len(self.visited) != n:
            return False

        return True