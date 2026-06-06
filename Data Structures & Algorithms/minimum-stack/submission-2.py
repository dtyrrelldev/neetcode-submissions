class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        element = self.stack[-1]
        return element

    def getMin(self) -> int:
        if self.stack:
            lowest = min(self.stack)
            return lowest
        

        
