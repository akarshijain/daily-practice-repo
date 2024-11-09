class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token_stack = []

        for token in tokens:
            if token in "+-*/":
                num1 = token_stack.pop()
                num2 = token_stack.pop()

                if token == "*":
                    token_stack.append(num2 * num1)
                elif token == "/":
                    token_stack.append(int(num2 / num1))
                elif token == "+":
                    token_stack.append(num2 + num1)
                elif token == "-":
                    token_stack.append(num2 - num1)
            else:
                token_stack.append(int(token))    

        return token_stack[-1]

                
        