class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:return s
        t=(numRows-1)*2
        i=0
        c=0
        ans=''
        print(f'String len: {len(s)} and {(numRows-1)*2}')
        while True:
            if i==numRows:return ans
            if c>=len(s):
                i+=1
                c=i
                t-=2
                continue
            # gap=abs(t-((numRows-1)*2))
            # if gap!=((numRows-1)*2):
            #     ans+=s[c+t]
            # print(c,end=' ')
            ans+=s[c]
            # print((c+((numRows-1)*2)-(i*2)),i,end=' ')
            # print((c+((numRows-1)*2)-(i*2))<len(s))
            if i!=0 and i!=(numRows-1) and ((c+((numRows-1)*2)-(i*2))<len(s)):
                ans+=s[(c+((numRows-1)*2)-(i*2))]
            c+=(numRows-1)*2
