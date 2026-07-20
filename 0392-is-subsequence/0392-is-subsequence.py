class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while(i<len(s) and j<len(t)):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i==len(s)
        # it is right trying another way
        # for i in range(len(s)):
        #     if s[i] in t:
        #         t=t[(t.index(s[i])+1):]
        #     else:
        #         return False
        # return True
        # it is right trying another way
