class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        for i in grid:
            l.extend(i)
        for i in range(k):
            l.insert(0,l[-1])
            l.pop(-1)
        print(l)
        arr=[l[i:i+len(grid[0])] for i in range(0,len(l),len(grid[0]))]
        return arr
