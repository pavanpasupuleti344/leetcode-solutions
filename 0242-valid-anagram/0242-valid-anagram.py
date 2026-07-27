class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        a.sort()
        b=list(t)
        b.sort()
        print(a)
        print(b)
        return ("".join(a))==("".join(b))