class Solution:
    def countCommas(self, n: int) -> int:
        num='1000'
        # digits=len(str(n))
        def com(n):
            digits=len(str(n))
            comas=0
            if digits%3==0:
                comas=(digits//3)-1
            else:
                comas=digits//3
            return comas
        
        if com(n)==0:return 0
        # print('hi')
        ans=0
        while True:
            if n-int(num)>=0:
                # ans+=(n-int(num)+1)*com(int(num))
                ans+=(n-int(num)+1)*1
                num+='000'
            else:
                break
        return ans
