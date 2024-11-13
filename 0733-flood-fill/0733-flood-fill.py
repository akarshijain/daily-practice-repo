class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        image[sr][sc] = color

        pixel_q = deque()
        pixel_q.append((sr, sc))

        visited = set()
        visited.add((sr, sc))

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while pixel_q:
            curr_row, curr_col = pixel_q.popleft()
            for dr, dc in directions:
                new_row = curr_row + dr
                new_col = curr_col + dc

                if not new_row in range(len(image)) or \
                    not new_col in range(len(image[0])) or \
                    (new_row, new_col) in visited or \
                    image[new_row][new_col] != original_color:
                    continue


                image[new_row][new_col] = color
                pixel_q.append((new_row, new_col))
                visited.add((new_row, new_col))

        return image