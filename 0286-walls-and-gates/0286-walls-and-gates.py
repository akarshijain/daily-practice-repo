class Solution:
    def __init__(self):
        pass
    
    def fillEmptyRooms(self, row, col, grid):
        visited = set()
        visited.add((row, col))

        rooms_q = deque()
        rooms_q.append((row, col))

        distance = 1

        while rooms_q:
            for i in range(len(rooms_q)):
                old_row, old_col = rooms_q.popleft()

                directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                for dr, dc in directions:
                    new_row, new_col = old_row + dr, old_col + dc

                    if new_row not in range(len(grid)) \
                        or new_col not in range(len(grid[0])) \
                        or (new_row, new_col) in visited \
                        or grid[new_row][new_col] == -1 \
                        or grid[new_row][new_col] == 0:
                        continue

                    visited.add((new_row, new_col))
                    rooms_q.append((new_row, new_col))
                    grid[new_row][new_col] = min(grid[new_row][new_col], distance)

            distance += 1
            

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    self.fillEmptyRooms(row, col, rooms)
        