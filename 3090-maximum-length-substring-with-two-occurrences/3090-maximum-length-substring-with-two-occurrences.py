class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i=0
        j=0
        d={}
        maxi=0
        while(j<len(s)):
            d[s[j]]=d.get(s[j],0)+1
            while 3 in d.values():
                d[s[i]]-=1
                i+=1
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi