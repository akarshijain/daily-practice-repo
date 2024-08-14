class Solution:
    def __init__(self):
        self.area = 0
        self.visit = set()

    def bfs(self, row, col, grid):
        area = 1
        island = collections.deque()

        island.append((row, col))
        self.visit.add((row, col))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while island:
            r, c = island.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc

                if row in range(len(grid)) \
                    and col in range(len(grid[0])) \
                    and grid[row][col] == 1 \
                    and (row, col) not in self.visit:

                    island.append((row, col))
                    self.visit.add((row, col))

                    area += 1

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in self.visit:
                    self.area = max(self.area, self.bfs(i, j, grid))

        return self.area