class Solution:
    def __init__(self):
        self.visit = set()
        self.count = 0
    
    def bfs(self, grid, r, c):
        island_q = collections.deque()
        island_q.append((r, c))

        self.visit.add((r, c))

        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        while island_q:
            for i in range(len(island_q)):
                r, c = island_q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(len(grid)) \
                            and col in range(len(grid[0])) \
                            and grid[row][col] == "1" \
                            and (row, col) not in self.visit:
                        island_q.append((row, col))
                        self.visit.add((row, col))

    def numIslands(self, grid: List[List[str]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in self.visit:
                    self.bfs(grid, r, c)
                    self.count += 1

        return self.count