class Solution:
    def __init__(self):
        self.max_area = 0
        self.visited = set()
        self.island_q = deque()

    def calculateIslandArea(self, row, col, grid):
        area = 1

        self.island_q.append((row, col))
        self.visited.add((row, col))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while self.island_q:
            curr_row, curr_col = self.island_q.popleft()
            for dr, dc in directions:
                new_row, new_col = curr_row + dr, curr_col + dc

                if new_row not in range(len(grid)) or \
                    new_col not in range(len(grid[0])) or \
                    (new_row, new_col) in self.visited or \
                    grid[new_row][new_col] == 0:
                    continue

                area += 1
                self.island_q.append((new_row, new_col))
                self.visited.add((new_row, new_col))
                
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in self.visited:
                    self.max_area = max(self.max_area, self.calculateIslandArea(row, col, grid))

        return self.max_area
