class Solution:
    def __init__(self):
        self.atlanticOcean = set()
        self.pacificOcean = set()

    def dfs(self, row, col, heights, ocean, prevHeight):
        if (row, col) in ocean \
            or row not in range(len(heights)) \
            or col not in range(len(heights[0])) \
            or heights[row][col] < prevHeight:
            return
        
        ocean.add((row, col))
        self.dfs(row - 1, col, heights, ocean, heights[row][col])
        self.dfs(row + 1, col, heights, ocean, heights[row][col])
        self.dfs(row, col - 1, heights, ocean, heights[row][col])
        self.dfs(row, col + 1, heights, ocean, heights[row][col])

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        for row in range(ROWS):
            self.dfs(row, 0, heights, self.pacificOcean, heights[row][0])
            self.dfs(row, COLS - 1, heights, self.atlanticOcean, heights[row][COLS - 1])

        for col in range(COLS):
            self.dfs(0, col, heights, self.pacificOcean, heights[0][col])
            self.dfs(ROWS - 1, col, heights, self.atlanticOcean, heights[ROWS - 1][col])

        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in self.pacificOcean and (i, j) in self.atlanticOcean:
                    result.append([i, j])

        return result