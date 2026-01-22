class Solution {
    public void setZeroes(int[][] matrix) {
        ArrayList<Integer> col=new ArrayList<>();
        ArrayList<Integer> row=new ArrayList<>();
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[i].length;j++){
                if(matrix[i][j]==0){
                    col.add(j);
                    row.add(i);
                }
            }
        }
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[i].length;j++){
                if(row.contains(i)){
                    Arrays.fill(matrix[i],0);
                }
                if(col.contains(j)){
                    matrix[i][j]=0;
                }
            }
        }
    }
}