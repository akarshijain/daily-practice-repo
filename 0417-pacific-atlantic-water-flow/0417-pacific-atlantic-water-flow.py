class Solution:
    def canReachOcean(self, row, col, grid):
        cell_q = deque()
        cell_q.append((row, col))

        visited = set()
        visited.add((row, col))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while cell_q:
            old_row, old_col = cell_q.popleft()
            for dr, dc in directions:
                new_row, new_col = old_row + dr, old_col + dc
                if new_row not in range(len(grid)) or \
                    new_col not in range(len(grid[0])) or \
                    (new_row, new_col) in visited or \
                    grid[new_row][new_col] < grid[old_row][old_col]:
                    continue

                cell_q.append((new_row, new_col))
                visited.add((new_row, new_col))

        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific_ocean_islands = []
        for col in range(n):
            pacific_ocean_islands.append([0, col])

        for row in range(1, m):
            pacific_ocean_islands.append([row, 0])

        atlantic_ocean_islands = []
        for col in range(0, n):
            atlantic_ocean_islands.append([m - 1, col])

        for row in range(0, m-1):
            atlantic_ocean_islands.append([row, n - 1])
            
        pacific_cells = set()
        for row, col in pacific_ocean_islands:
            pacific_cells.update(self.canReachOcean(row, col, heights))

        atlantic_cells = set()
        for row, col in atlantic_ocean_islands:
            atlantic_cells.update(self.canReachOcean(row, col, heights))

        result = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in pacific_cells and \
                    (row, col) in atlantic_cells:
                    result.append([row, col])
        
        return result