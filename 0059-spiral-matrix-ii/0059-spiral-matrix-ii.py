class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l=[[0]*n for i in range(n)]
        top=0
        bottom=n-1
        left=0
        right=n-1
        k=1
        while(left<=right and top<=bottom):
            for i in range(left,right+1):
                l[top][i]=k
                k=k+1
            top=top+1
            if(top>bottom):break
            for i in range(top,bottom+1):
                l[i][right]=k
                k=k+1
            right=right-1
            if(left>right):break
            for i in range(right,left-1,-1):
                l[bottom][i]=k
                k=k+1
            bottom=bottom-1
            for i in range(bottom,top-1,-1):
                l[i][left]=k
                k=k+1
            left=left+1
        return l