class Logger:

    def __init__(self):
        self.time_limit = 10
        self.next_timestamp = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.next_timestamp or \
                 self.next_timestamp[message] <= timestamp:
            print(message)
            self.next_timestamp[message] = timestamp + self.time_limit
            return True

        return False
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)