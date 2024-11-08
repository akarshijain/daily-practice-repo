class Solution:
    def isValid(self, strs: str) -> bool:
        parenthesis_stack = []

        for s in strs:
            if not parenthesis_stack and (s == ")" or s == "}" or s == "]"):
                return False

            if s == "(" or s == "{" or s == "[":
                parenthesis_stack.append(s)

            elif s == ")" and parenthesis_stack[-1] == "(":
                parenthesis_stack.pop()

            elif s == "]" and parenthesis_stack[-1] == "[":
                parenthesis_stack.pop()

            elif s == "}" and parenthesis_stack[-1] == "{":
                parenthesis_stack.pop()
                
            else:
                return False
        
        if parenthesis_stack:
            return False

        return True

        

        