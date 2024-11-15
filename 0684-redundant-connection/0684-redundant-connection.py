class Solution:
    def dfs(self, node, prev, adj_list, visited):
        if node in visited:
            return True

        visited.add(node)

        for nei in adj_list[node]:
            if nei == prev:
                continue

            if self.dfs(nei, node, adj_list, visited):
                return True

        return False


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = {}

        for i in range(len(edges)):
            adj_list[i+1] = []

        for node, nei in edges:
            adj_list[node].append(nei)
            adj_list[nei].append(node)

            visited = set()
            if self.dfs(node, 0, adj_list, visited):
                return [node, nei]

        return []
        
        