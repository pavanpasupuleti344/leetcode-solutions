class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        k=k%(len(grid)*len(grid[0]))
        l=[]
        for i in grid:
            l.extend(i)
        # for i in range(k):
        #     l.insert(0,l[-1])
        #     l.pop(-1)
        # l2=l[(len(l)-k):]
        # l2+=l[0:(len(l)-k)]
        # l=l2
        l=l[-k:]+l[:-k]
        arr=[l[i:i+len(grid[0])] for i in range(0,len(l),len(grid[0]))]
        return arr
