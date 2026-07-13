class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s='123456789'
        i=0
        k=0
        j=len(str(low))+k
        l=[]
        while int(s[i:j])<=high:
            if s[i:j][-1]=='9':
                l.append(int(s[i:j]))
                i=0
                k=k+1
                j=len(str(low))+k
                if j>9:break
            else:
                l.append(int(s[i:j]))
                i=i+1
                j=j+1 
        return [n for n in l if n in range(low,high+1)]
        # i=0
        # l=[]
        # s='123456789'
        # m='111111111'
        # n=int(s[0:len(str(low))+i])
        # n2=int(m[0:len(str(low))+i])
        # while n in range(n,high+1):
        #     if(str(n)[-1]=='9'):
        #         l.append(n)
        #         i=i+1
        #         n=int(s[0:len(str(low))+i])
        #         n2=int(m[0:len(str(low))+i])
        #     else:
        #         l.append(n)
        #         n=n+n2
        # r=[k for k in l if k in range(low,high+1)]
        # return r
        