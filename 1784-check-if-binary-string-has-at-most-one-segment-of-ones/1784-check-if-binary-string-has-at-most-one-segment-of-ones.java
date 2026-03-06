class Solution {
    public boolean checkOnesSegment(String s) {
        if(s.length()==1){return true;}
        int count =0;
        int contOne=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='1'){
                contOne++;
            }
            else{
                if(contOne>=1){count++;}
                contOne=0;
            }
        }
        if(contOne>=1){count++;}
        return count==1;
    }
}