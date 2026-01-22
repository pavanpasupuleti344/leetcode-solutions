class Solution {
    public int myAtoi(String s) {
        String n=s.trim();
        int k=0;
        int a=1;
        long ans=0;
        if(n.length()==0){
            return 0;
        }
        if(n.charAt(0)=='+'){
            a=1;
            k=1;
        }
        if(n.charAt(0)=='-'){
            a=-1;
            k=1;
        }
        while(k<n.length()&&n.charAt(k)>='0'&&n.charAt(k)<='9'){
            ans*=10;
            ans+=n.charAt(k)-'0';
            if(ans*a<=Integer.MIN_VALUE){return Integer.MIN_VALUE;}
            else if(ans*a>=Integer.MAX_VALUE){return Integer.MAX_VALUE;}
            k++;
        }
        ans*=a;
        return (int)ans;
    }
}