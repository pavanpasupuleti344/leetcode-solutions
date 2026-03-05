class Solution {
    public int minOperations(String s) {
        StringBuilder fo=new StringBuilder();
        StringBuilder fz=new StringBuilder();
        int firstOne=0;
        int firstZero=0;
        for(int i=0;i<s.length();i++){
            if(i%2==0){
                fo.append('1');
                fz.append('0');
            }
            else{
                fo.append('0');
                fz.append('1');
            }
        }
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)!=fo.charAt(i)){firstOne++;}
            if(s.charAt(i)!=fz.charAt(i)){firstZero++;}
        }
        return Math.min(firstOne,firstZero);
    }
}