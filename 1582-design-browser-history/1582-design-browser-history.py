class ListNode:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.home.next = newNode
        newNode.prev = self.home
        self.home = newNode

    def back(self, steps: int) -> str:
        while steps > 0 and self.home.prev:
            self.home = self.home.prev
            steps -= 1
        return self.home.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.home.next:
            self.home = self.home.next
            steps -= 1
        return self.home.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)