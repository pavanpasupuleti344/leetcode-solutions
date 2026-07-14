class Solution:
    def maxPower(self, s: str) -> int:
        last=s[0]
        c=1
        ans=1
        for i in range(1,len(s)):
            if s[i]==last:
                last=s[i]
                c=c+1
            else:
                last=s[i]
                ans=max(ans,c)
                c=1
        return max(ans,c)