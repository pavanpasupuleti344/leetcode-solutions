class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> ans=new ArrayList<>();
        for(int i=0;i<rowIndex+1;i++){
            List<Integer> sol=new ArrayList<>();
            for(int j=0;j<=i;j++){
                if(j==0||j==i){
                    sol.add(1);
                }
                else{
                    sol.add((ans.get(i-1)).get(j)+(ans.get(i-1)).get(j-1));
                }
            }
            ans.add(new ArrayList<>(sol));
        }
        return ans.get(rowIndex);
    }
}