class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_val_stack = []

    def push(self, val: int) -> None:
        if not self.min_val_stack:
            self.min_val_stack.append(val)
        else:
            self.min_val_stack.append(min(self.min_val_stack[-1], val))

        self.min_stack.append(val)

    def pop(self) -> None:
        self.min_val_stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.min_stack[-1]
        
    def getMin(self) -> int:
        return self.min_val_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()