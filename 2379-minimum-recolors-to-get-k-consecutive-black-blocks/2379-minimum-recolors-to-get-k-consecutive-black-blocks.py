class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c=0
        for i in range(k):
            if blocks[i]=='B':
                c+=1
        i,j,m=1,k,c
        while(j<len(blocks)):
            if blocks[i-1]=='B':
                c-=1
            if blocks[j]=='B':
                c+=1
            i+=1
            j+=1
            m=max(m,c)
        return k-m