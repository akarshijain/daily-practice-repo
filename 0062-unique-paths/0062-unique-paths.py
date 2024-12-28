class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        unique_paths = [[1] * n] * m

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                unique_paths[i][j] = unique_paths[i+1][j] + unique_paths[i][j+1]


        return unique_paths[0][0]