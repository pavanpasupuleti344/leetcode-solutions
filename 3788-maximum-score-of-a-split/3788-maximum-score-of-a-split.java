class Solution {
    public long maximumScore(int[] nums) {
        long[] pi=new long[nums.length];
        for(int i=0;i<nums.length;i++){
            if(i==0){pi[i]=nums[i];}
            else pi[i]=pi[i-1]+nums[i];
        }
        int m=nums[nums.length-1];
        for(int i=nums.length-1;i>=0;i--){
            nums[i]=Math.min(m,nums[i]);
            m=nums[i];
        }
        int start=0;
        long value=Long.MIN_VALUE;
        for(int i=start;i<nums.length-1;i++){
            long diff=pi[i]-nums[i+1];
            value=Math.max(value,diff);
        }
        return value;
    }
}