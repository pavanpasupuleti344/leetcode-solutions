class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):return False
        s,d={},{}
        for i in range(len(s1)):
            s[s1[i]]=s.get(s1[i],0)+1
            d[s2[i]]=d.get(s2[i],0)+1
        if s==d:return True
        i=0
        j=len(s1)-1
        while(j<len(s2)-1):
            d[s2[i]]-=1
            if d[s2[i]]==0:d.pop(s2[i])
            i+=1
            j+=1
            d[s2[j]]=d.get(s2[j],0)+1
            if s==d : 
                return True
        return False