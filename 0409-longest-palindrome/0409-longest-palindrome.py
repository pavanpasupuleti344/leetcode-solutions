class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        odd=0
        sumi=0
        for c in s:
            d[c]=d.get(c,0)+1
        sumi+=sum(map(lambda x:(x//2)*2,d.values()))
        if any(x%2!=0 for x in d.values()):
            odd+=1
        return sumi+odd