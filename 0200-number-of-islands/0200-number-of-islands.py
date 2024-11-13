class Solution:
    def __init__(self):
        self.count = 0
        self.visited = set()
        self.island_q = deque()

    def countIslands(self, row, col, grid):
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        self.island_q.append((row, col))
        self.visited.add((row, col))

        while self.island_q:
            old_row, old_col = self.island_q.popleft()
            for dr, dc in directions:
                new_row = old_row + dr
                new_col = old_col + dc

                if new_row not in range(len(grid)) or \
                    new_col not in range(len(grid[0])) or \
                    (new_row, new_col) in self.visited or \
                    grid[new_row][new_col] == "0":
                    continue

                self.island_q.append((new_row, new_col))
                self.visited.add((new_row, new_col))

    def numIslands(self, grid: List[List[str]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.count += 1
                    self.countIslands(row, col, grid)

        return self.count
