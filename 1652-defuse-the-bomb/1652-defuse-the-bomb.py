class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k==0:return [0]*len(code)
        n=len(code)
        ans=[]
        for i in range(len(code)):
            sumi=0
            if k>0:
                print(i+1,i+1+k)
                ans.append(sum([code[j%n] for j in range(i+1,i+k+1)]))
                # for j in range(i+1,i+k+1):
                #     sumi+=code[j%n]
                # ans.append(sumi)
            else:
                print()                                       #i 0    1
                for j in range(1,abs(k)+1):              # j 1,2  1,2
                    print((n-j+i)%n,end=' ')              #   3: 3,2 2 
                    sumi+=code[(n-j+i)%n]
                ans.append(sumi)


        return ans