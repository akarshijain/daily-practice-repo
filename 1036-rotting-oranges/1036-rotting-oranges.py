class Solution:

    def __init__(self):
        self.minutes = 0
        self.fresh_oranges = 0
        self.orange_q = collections.deque()

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.fresh_oranges += 1
                if grid[r][c] == 2:
                    self.orange_q.append((r, c))

        while self.fresh_oranges > 0 and self.orange_q:
            for i in range(len(self.orange_q)):
                r, c = self.orange_q.popleft()
                directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row in range(len(grid)) \
                        and col in range(len(grid[0])) \
                        and grid[row][col] == 1:

                        grid[row][col] = 2
                        self.fresh_oranges -= 1
                        self.orange_q.append((row, col))

            self.minutes += 1

        if self.fresh_oranges:
            return -1
            
        return self.minutes
