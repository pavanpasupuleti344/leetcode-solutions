class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        for c in s:
            d[c]=d.get(c,0)+1
            if d[c]==2:
                return c