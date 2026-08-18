class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cln=set()
        row=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    row.add(i)
                    cln.add(j)
        print(row)
        print(cln)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row or j in cln:
                    matrix[i][j]=0
        return matrix