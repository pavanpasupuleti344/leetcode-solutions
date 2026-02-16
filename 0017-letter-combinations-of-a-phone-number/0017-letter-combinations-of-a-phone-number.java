class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> ans=new ArrayList<>();
        String[] let={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        StringBuilder res=new StringBuilder();
        return answer(digits,let,ans,res,0);   
    }
    private List<String> answer(String b,String[] let,List<String> ans,StringBuilder res,int index){
        if(index==b.length()){ans.add(res.toString());return ans;}
        int j=b.charAt(index)-'0';
        for(int i=0;i<let[j].length();i++){
            res.append(let[j].charAt(i));
            answer(b,let,ans,res,index+1);
            res.deleteCharAt(res.length()-1);
        }
        return ans;
        // StringBuilder res=new StringBuilder();
    }
}