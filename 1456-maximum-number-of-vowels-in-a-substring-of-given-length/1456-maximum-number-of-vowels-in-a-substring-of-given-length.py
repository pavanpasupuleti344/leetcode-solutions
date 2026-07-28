class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v='aeiou'
        c=0
        for i in range(k):
            if s[i] in v:
                c+=1
        i=1
        j=k
        m=c
        while j<len(s):
            if s[i-1] in v:
                c-=1
            if s[j] in v:
                c+=1
            i+=1
            j+=1
            m=max(m,c)
        return m

        # v='aeiou'
        # m=0
        # i,j=0,k-1
        # while j<len(s):
        #     s=sum(1 for x in s[i:j+1] if x in v )
        #     m=max(m,s)
        # return m