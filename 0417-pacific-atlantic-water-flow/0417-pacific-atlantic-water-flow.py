class Solution:
    def get_cells_can_reach(self, row, col, heights):
        visited = set()
        visited.add((row, col))

        cell_q = deque()
        cell_q.append((row, col))

        while cell_q:
            old_row, old_col = cell_q.popleft()
            directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
            for dr, dc in directions:
                new_row, new_col = old_row + dr, old_col + dc

                if new_row not in range(len(heights)) \
                    or new_col not in range(len(heights[0])) \
                    or (new_row, new_col) in visited \
                    or heights[new_row][new_col] < heights[old_row][old_col]:
                    continue

                visited.add((new_row, new_col))
                cell_q.append((new_row, new_col))

        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_ocean_boundary = set()
        atlantic_ocean_boundary = set()

        for row in range(len(heights)):
            pacific_ocean_boundary.add((row, 0))
            atlantic_ocean_boundary.add((row, len(heights[0]) - 1))

        for col in range(len(heights[0])):
            pacific_ocean_boundary.add((0, col))
            atlantic_ocean_boundary.add((len(heights) - 1, col))

        cells_reach_pacific = set()
        for row, col in pacific_ocean_boundary:
            cells_reach_pacific.update(self.get_cells_can_reach(row, col, heights))

        cells_reach_atlantic = set()
        for row, col in atlantic_ocean_boundary:
            cells_reach_atlantic.update(self.get_cells_can_reach(row, col, heights))

        result = set()
        result = cells_reach_pacific.intersection(cells_reach_atlantic)

        return list(result)
