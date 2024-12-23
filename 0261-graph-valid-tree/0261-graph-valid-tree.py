class Solution:
    def __init__(self):
        self.visited = set()
    
    def dfs(self, curr_node, prev_node, adj_list):
        if curr_node in self.visited:
            return False

        self.visited.add(curr_node)

        for neighbor in adj_list[curr_node]:
            if neighbor == prev_node:
                continue

            if not self.dfs(neighbor, curr_node, adj_list):
                return False

        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []

        for node, neighbor in edges:
            adj_list[node].append(neighbor)
            adj_list[neighbor].append(node)

        if not self.dfs(0, -1, adj_list):
            return False

        return len(self.visited) == n