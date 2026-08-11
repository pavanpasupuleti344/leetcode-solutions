class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0
        col=-1
        for i in range(len(matrix[0])):
            if matrix[row][i]>target:
                col=i-1
                break
        else:col=len(matrix[0])-1
        # print(col)
        cln=0
        for i in range(len(matrix)):
            if matrix[i][cln]>target:
                row=i-1
                break
        else:
            row=len(matrix)-1
        # print(row,col)
        for i in range(row+1):
            for j in range(col+1):
                if matrix[i][j]==target:
                    return True
        return False