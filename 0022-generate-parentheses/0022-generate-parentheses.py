class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def isValid(self, bracket):
        bracket_st = []
        for b in bracket:
            if not bracket_st and b == ")":
                return False

            if b == "(":
                bracket_st.append(b)
            elif b == ")" and bracket_st[0] == "(":
                bracket_st.pop()
            else:
                return False

        if bracket_st:
            return False

        return True

    def dfs(self, index, n):
        if index >= 2*n:
            bracket = "".join(self.path)
            if self.isValid(bracket):
                self.result.append(bracket)
            return
        
        for bracket in "()":
            self.path.append(bracket)
            self.dfs(index + 1, n)
            self.path.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs(0, n)

        return self.result
        