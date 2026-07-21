class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        l=list(s)
        c=l.count(y)
        while(y in l):
            l.remove(y)
        a=c*y
        a+="".join(l)
        return a