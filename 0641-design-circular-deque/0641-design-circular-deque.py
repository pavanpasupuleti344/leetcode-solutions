class MyCircularDeque:

    def __init__(self, k: int):
        self.d=[None]*k
        self.k=k
        self.size=0
        self.front=self.rear=0

    def insertFront(self, value: int) -> bool:
        if self.size==self.k:
            return False
        self.size+=1
        self.front=(self.front-1)%self.k
        if self.front<0:
            self.front+=len(self.d)
        self.d[self.front]=value
        return True

    def insertLast(self, value: int) -> bool:
        if self.size==self.k:
            return False
        self.d[self.rear]=value
        self.size+=1
        self.rear=(self.rear+1)%self.k
        return True

    def deleteFront(self) -> bool:
        if self.size==0:
            return False
        self.size-=1
        self.front=(self.front+1)%self.k
        return True

    def deleteLast(self) -> bool:
        if self.size==0:
            return False
        self.size-=1
        # self.front=(self.front-1)%self.k
        self.rear=(self.rear-1)%self.k
        if self.rear<0:
            self.rear=len(self.d)-1
        return True

    def getFront(self) -> int:
        if self.size==0:
            return -1
        return self.d[self.front]

    def getRear(self) -> int:
        if self.size==0:
            return -1
        return self.d[self.rear-1]

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()