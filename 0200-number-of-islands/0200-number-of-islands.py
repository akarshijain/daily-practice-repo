class Solution:
    def __init__(self):
        self.visit = set()
        self.num_island = 0
    
    def bfs(self, row, col, grid):
        island_q = deque()
        island_q.append((row, col))

        self.visit.add((row, col))

        while island_q:
            old_row, old_col = island_q.popleft()
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                new_row, new_col = old_row + dr, old_col + dc

                if new_row not in range(len(grid)) \
                    or new_col not in range(len(grid[0])) \
                    or (new_row, new_col) in self.visit \
                    or grid[new_row][new_col] == "0":
                    continue

                self.visit.add((new_row, new_col))
                island_q.append((new_row, new_col))


    def numIslands(self, grid: List[List[str]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in self.visit:
                    self.bfs(row, col, grid)
                    self.num_island += 1

        return self.num_island