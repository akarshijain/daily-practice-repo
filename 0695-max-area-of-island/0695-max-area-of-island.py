class Solution:
    def __init__(self):
        self.visit = set()

    def bfs(self, grid, row, col):

        area = 1
        self.visit.add((row, col))

        island_q = collections.deque()
        island_q.append((row, col))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while island_q:
            r, c = island_q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(len(grid)) and col in range(len(grid[0])) \
                                   and grid[row][col] == 1 \
                                   and (row, col) not in self.visit:
                    area += 1
                    self.visit.add((row, col))
                    island_q.append((row, col))

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in self.visit:
                    area = max(area, self.bfs(grid, r, c))

        return area


        