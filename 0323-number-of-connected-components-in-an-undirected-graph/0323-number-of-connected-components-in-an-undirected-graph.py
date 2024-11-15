class Solution:
    def __init__(self):
        self.visited = set()

    def dfs(self, node, prev, neighbors_map):
        self.visited.add(node)

        for nei in neighbors_map[node]:
            if nei == prev or nei in self.visited:
                continue

            self.dfs(nei, node, neighbors_map)

        return 

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors_map = {}

        for i in range(n):
            neighbors_map[i] = []

        for node, nei in edges:
            neighbors_map[node].append(nei)
            neighbors_map[nei].append(node)

        count = 0
        for node in neighbors_map:
            if node in self.visited:
                continue
            count += 1
            self.dfs(node, -1, neighbors_map)

        return count
