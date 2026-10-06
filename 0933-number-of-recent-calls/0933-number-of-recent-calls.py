class RecentCounter:

    def __init__(self):
        self.l=[]

    def ping(self, t: int) -> int:
        self.l.append(t)
        while self.l and self.l[0] not in range(t-3000,t+1):
            self.l.pop(0)
        return len(self.l)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)