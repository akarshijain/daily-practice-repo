class Solution:
    def judgeCircle(self, moves: str) -> bool:
        right = 0
        up = 0
        for move in moves:
            if move == "R":
                right += 1
            if move == "L":
                right -= 1
            if move == "U":
                up += 1
            if move == "D":
                up -= 1
        
        if up == 0 and right == 0:
            return True
        
        return False