class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1

        rotten_oranges = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))

        time = 0
        while rotten_oranges and fresh_oranges:
            for i in range(len(rotten_oranges)):
                r, c = rotten_oranges.popleft()

                directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(len(grid)) \
                        and col in range(len(grid[0])) \
                        and grid[row][col] == 1:

                        grid[row][col] = 2
                        rotten_oranges.append((row, col))
                        fresh_oranges -= 1

            time += 1

        if fresh_oranges:
            return -1

        return time
