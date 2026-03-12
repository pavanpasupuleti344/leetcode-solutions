class Solution {
    public List<String> generateParenthesis(int n) {
        return ans("",n,0,0);
    }
    private List<String> ans(String up,int n,int l,int r){
        if(r==n&&l==n){
            List<String> list=new ArrayList<>();
            list.add(up);
            return list;
        }
        List<String> list=new ArrayList<>();
        if(l<n){
            list.addAll(ans(up+"(",n,l+1,r));
        }
        if(r<l){
            list.addAll(ans(up+")",n,l,r+1));
        }
        return list;
    }
}