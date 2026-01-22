class Solution {
    public int sumFourDivisors(int[] nums) {
        int sum=0;
        for(int i:nums){
            sum+=div(i);
        }
        return sum;
    }
    private static int div(int n){
        int c=0;
        int sum=0;
        for(int i=1;i<=Math.sqrt(n);i++){
            if(n%i!=0){continue;}
            if(n/i==i){c+=1;sum+=i;}
            else{c+=2;sum+=i+(n/i);}
            if(c>4) return 0;
        }
        if(c==4)return sum;
        return 0;
    }
}