class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        distance = 0
        visit = set()
        gates = collections.deque()

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gates.append((i, j))

        while gates:
            distance += 1
            for i in range(len(gates)):
                r, c = gates.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row not in range(len(rooms)) \
                        or col not in range(len(rooms[0])) \
                        or (row, col) in visit \
                        or rooms[row][col] == -1 \
                        or rooms[row][col] == 0:
                        continue
                    
                    rooms[row][col] = distance
                    gates.append((row, col))
                    visit.add((row, col))

