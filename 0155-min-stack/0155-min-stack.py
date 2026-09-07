class MinStack:

    def __init__(self):
        self.st=[]
        self.min=[]

    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.min:
            self.min.append(value)
        else:
            self.min.append(min(value,self.min[-1]))

    def pop(self) -> None:
        if not self.min:
            return
        self.min.pop()
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        # if not self.min:
        #     return
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()