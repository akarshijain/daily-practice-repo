class Solution:
    def __init__(self):
        self.parentheses = []
        self.all_combinations = []

    def isValidParentheses(self, bracket):
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

    def dfs(self, n):
        if len(self.parentheses) >= 2*n:
            if self.isValidParentheses(self.parentheses):
                self.all_combinations.append(''.join(self.parentheses.copy()))
            return

        self.parentheses.append("(")
        self.dfs(n)
        self.parentheses.pop()

        self.parentheses.append(")")
        self.dfs(n)
        self.parentheses.pop()

        return

    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs(n)
        return self.all_combinations