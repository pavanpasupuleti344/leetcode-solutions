class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=[]
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        # i=0 j=0
        while(left<=right and top<=bottom):
            for i in range(left,right+1):
                l.append(matrix[top][i])
            top=top+1
            if(top>bottom):break
            for i in range(top,bottom+1):
                l.append(matrix[i][right])
            right=right-1
            if(right<left):break
            for i in range(right,left-1,-1):
                l.append(matrix[bottom][i])
            bottom=bottom-1
            if(top>bottom):break
            for i in range(bottom,top-1,-1):
                l.append(matrix[i][left])
            left=left+1
            if(right<left):break
        return l