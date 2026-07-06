class MinStack:

    # 1 2 0 pop getMin 
    # stack = [1] min = [1]
    # stack = [1 2] min = [1]
    # stack = [1 2 0] min = [1 0]
    # stack = [1 2] min = [1]
    # getMin = 1
    
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # if stack is empty append the first value since thats the new min
        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]: # min stack is not empty so only add if it is less than the latest val
            self.minStack.append(val)


    def pop(self) -> None:
        # if the val being popped and top of minStack are the same, pop from the min stack as well
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()

        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
