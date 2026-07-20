class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        v='aeiou'
        # l=0
        j=len(s)-1
        i=0
        while(i<j):
            if l[i].lower() not in v:
                i+=1
            if l[j].lower() not in v:
                j-=1
            if(l[i].lower() in v and l[j].lower() in v):
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
        return "".join(map(str,l))