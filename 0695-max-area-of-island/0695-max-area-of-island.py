class Solution:
    def __init__(self):
        self.visit = set()
        self.max_area = 0

    def get_area_of_island(self, row, col, grid):
        area = 1

        self.visit.add((row, col))

        island_q = deque()
        island_q.append((row, col))

        while island_q:
            old_row, old_col = island_q.popleft()

            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                new_row, new_col = old_row + dr, old_col + dc

                if new_row not in range(len(grid)) \
                    or new_col not in range(len(grid[0])) \
                    or grid[new_row][new_col] == 0 \
                    or (new_row, new_col) in self.visit:
                    continue

                area += 1
                self.visit.add((new_row, new_col))
                island_q.append((new_row, new_col))

        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 \
                    and (row, col) not in self.visit:
                    area = self.get_area_of_island(row, col, grid)
                    self.max_area = max(self.max_area, area)

        return self.max_area