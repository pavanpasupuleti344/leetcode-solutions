class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=0
        if (low%2)==0:
            low=low+1
        if (high%2)==0:
            high=high-1
        d=high-low+1
        return (d//2)+1
    