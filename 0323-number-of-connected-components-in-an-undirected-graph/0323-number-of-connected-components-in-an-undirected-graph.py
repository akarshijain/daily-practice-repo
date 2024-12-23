class Solution:
    def __init__(self):
        self.visited = set()
    
    def dfs(self, curr_node, prev_node, adj_list):
        self.visited.add(curr_node)

        for neighbor in adj_list[curr_node]:
            if neighbor == prev_node or neighbor in self.visited:
                continue

            self.dfs(neighbor, curr_node, adj_list)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []

        for node, neighbor in edges:
            adj_list[node].append(neighbor)
            adj_list[neighbor].append(node)

        count = 0
        for i in range(n):
            if i in self.visited:
                continue
            count += 1
            self.dfs(i, -1, adj_list)

        return count