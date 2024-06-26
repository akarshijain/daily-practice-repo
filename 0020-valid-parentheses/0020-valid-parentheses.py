class Solution:
    def isValid(self, s: str) -> bool:
        isValid = []
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False
        for p in s:
            if p == ')' and isValid and isValid[-1] == '(':
                isValid.pop()
            elif p == ']' and isValid and isValid[-1] == '[':
                isValid.pop()
            elif p == '}' and isValid and isValid[-1] == '{':
                isValid.pop()
            else:
                isValid.append(p)
            

        if len(isValid) == 0:
            return True
        
        return False