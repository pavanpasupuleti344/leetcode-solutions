class Solution {
    public String longestPalindrome(String s) {
        return  ans(s,0,new StringBuilder());
    }
    private String ans(String s,int index,StringBuilder sb){
        if(index==s.length()){return sb.toString();}
        for(int i=s.length()-1;i>=index;i--){
            if((i-index+1)<sb.length()){break;}
            if(s.charAt(i)==s.charAt(index)){
                if(check(s,index,i)){
                    if(i-index+1>sb.length()){
                        sb.setLength(0);
                        sb.append(s,index,i+1);
                        // return sb.toString();
                    }
                }
                }
        }
        return ans(s,index+1,sb);
    }
    private Boolean check(String s,int index,int last){
        int first=index;
        // int last=s.length();
        while(first<last){
            if(s.charAt(first)!=s.charAt(last)){return false;}
            last--;
            first++;
        }
        return true;
    }
}