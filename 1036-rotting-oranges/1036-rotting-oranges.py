class Solution:
    def __init__(self):
        self.fresh_oranges = 0
        self.time = 0
        self.orange_q = deque()


    def orangesRotting(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.fresh_oranges += 1
                if grid[row][col] == 2:
                    self.orange_q.append((row, col))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while self.fresh_oranges > 0 and self.orange_q:
            for _ in range(len(self.orange_q)):
                curr_row, curr_col = self.orange_q.popleft()
                for dr, dc in directions:
                    new_row, new_col = curr_row + dr, curr_col + dc

                    if new_row not in range(len(grid)) or \
                        new_col not in range(len(grid[0])) or \
                        grid[new_row][new_col] == 0 or \
                        grid[new_row][new_col] == 2:
                        continue

                    grid[new_row][new_col] = 2
                    self.fresh_oranges -= 1
                    self.orange_q.append((new_row, new_col))

            self.time += 1
        
        if self.fresh_oranges == 0:
            return self.time
        
        return -1