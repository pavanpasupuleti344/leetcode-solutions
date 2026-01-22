class Solution {
    public int maxProduct(int[] nums) {
        int max=Integer.MIN_VALUE;
        int p=1;
        for(int i=0;i<nums.length;i++){
            p=1;
            for(int j=i;j<nums.length;j++){
                p*=nums[j];
                max=Math.max(max,p);
            }
        }
        return max;
    }}
    // static int p(int i,int j,int[] nums){
    //     int[] pi=new int[nums.length];
    //     pi[i]=nums[i];
    //     for(int k=i+1;k<=j;k++){
    //         pi[k]=pi[k-1]*nums[k];
    //     }
    //     return pi[j];
    // }
