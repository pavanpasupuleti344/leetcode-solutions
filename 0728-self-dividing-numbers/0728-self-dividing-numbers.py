class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left,right+1):
            if(len(str(i))==1):
                l.append(i)
            elif self.check(i):
                l.append(i)
        return l

    def check(self,i: int) ->bool:
        s=str(i)
        for j in range(len(s)):
            d=int(s[j])
            if(d==0 or (i%d)!=0):
                return False
        return True
