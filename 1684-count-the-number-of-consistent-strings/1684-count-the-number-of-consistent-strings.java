class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int cnt=0;
        int wrong=-1;
        for(String s:words){
            wrong=-1;
            for(int i=0;i<s.length();i++){
                if(allowed.indexOf(s.charAt(i))==-1){
                    wrong=0;
                    break;
                }
            }
            if(wrong==-1){cnt++;}
        }
        return cnt;
    }
}