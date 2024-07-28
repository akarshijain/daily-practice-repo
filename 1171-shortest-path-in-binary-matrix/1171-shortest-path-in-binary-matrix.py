class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] != 0 or grid[ROWS-1][COLS-1] != 0:
            return -1

        visit = set()
        cell_q = collections.deque()

        cell_q.append((0, 0))
        pathLen = 1

        while cell_q:
            for i in range(len(cell_q)):
                r, c = cell_q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return pathLen

                directions = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row not in range(ROWS) \
                            or col not in range(COLS) \
                            or grid[row][col] == 1 \
                            or (row, col) in visit:
                        continue

                    visit.add((row, col))
                    cell_q.append((row, col))
                
            pathLen += 1

        return -1