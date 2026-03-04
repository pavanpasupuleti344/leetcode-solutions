class Solution {
    public int numSpecial(int[][] mat) {
        int count=0;
        List<Integer> row=new ArrayList<>();
        List<Integer> col=new ArrayList<>();
        for(int i=0;i<mat.length;i++){
            for(int j=0;j<mat[i].length;j++){
                if(mat[i][j]==1){
                    row.add(i);
                    col.add(j);
                }
            }
        }
        // for(int i=0;i<mat.length;i++){
        //     for(int j=0;j<mat[i].length;j++){
        //         if(mat[i][j]==1&&Collections.frequency(row,i)==1&&Collections.frequency(col,j)==1){
        //             count++;
        //             break;
        //         }

        //     }
        // }
        for(int i=0;i<row.size();i++){
            if(Collections.frequency(row,row.get(i))==1&&Collections.frequency(col,col.get(i))==1){
                count++;
            }
        }
        return count;
    }
}