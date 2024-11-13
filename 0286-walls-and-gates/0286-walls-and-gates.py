class Solution:
    def __init__(self):
        self.room_q = deque()

    def calculateNearestGate(self, row, col, grid):
        level = 1
        visited = set()
        self.room_q.append((row, col))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while self.room_q:
            for _ in range(len(self.room_q)):
                curr_row, curr_col = self.room_q.popleft()
                for dr, dc in directions:
                    new_row, new_col = curr_row + dr, curr_col + dc

                    if new_row not in range(len(grid)) or \
                        new_col not in range(len(grid[0])) or \
                        (new_row, new_col) in visited or \
                        grid[new_row][new_col] == -1 or \
                        grid[new_row][new_col] == 0:

                        continue

                    grid[new_row][new_col] = min(grid[new_row][new_col], level)
                    self.room_q.append((new_row, new_col))
                    visited.add((new_row, new_col))
            level += 1


    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    self.calculateNearestGate(row, col, rooms)
        