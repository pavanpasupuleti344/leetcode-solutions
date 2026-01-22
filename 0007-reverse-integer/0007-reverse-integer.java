class Solution {
    public int reverse(int x) {
        double max=Math.pow(2,31)-1;
        double min=Math.pow(2,31)*-1;
        long n=x;
        long r=0;
        if(n<0){n*=-1;}
        while(n>0){
            r*=10;
            r+=n%10;
            n=n/10;
        }
        if(x<0){
            r*=-1;
        }
        if(r>max||r<min){return 0;}
        else return (int)r;
    }
}