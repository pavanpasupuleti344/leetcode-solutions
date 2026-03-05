class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans=new ArrayList<>();
        // List<Integer> ready=new ArrayList<>();
        // ready.add(1);
        for(int i=0;i<numRows;i++){
            // int size=i;
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
        return ans;
    }
}