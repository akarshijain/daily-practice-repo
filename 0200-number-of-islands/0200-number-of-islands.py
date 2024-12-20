class Solution:
    def __init__(self):
        self.num_islands = 0
        self.visited = set()

    def connectIsland(self, row, col, grid):
        self.num_islands += 1

        self.visited.add((row, col))

        island_q = deque()
        island_q.append((row, col))

        while island_q:
            old_row, old_col = island_q.popleft()

            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                new_row, new_col = old_row + dr, old_col + dc

                if new_row not in range(len(grid)) \
                    or new_col not in range(len(grid[0])) \
                    or (new_row, new_col) in self.visited \
                    or grid[new_row][new_col] == "0":
                    continue

                self.visited.add((new_row, new_col))
                island_q.append((new_row, new_col))

    def numIslands(self, grid: List[List[str]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" \
                    and (row, col) not in self.visited:
                    self.connectIsland(row, col, grid)

        return self.num_islands
        