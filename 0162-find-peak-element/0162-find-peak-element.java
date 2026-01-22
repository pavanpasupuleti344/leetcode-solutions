class Solution {
    public int findPeakElement(int[] nums) {
        int max=Integer.MIN_VALUE;;
        int i=0;
        int pos=0;
        for(int k:nums){
            if(k>=max){max=k;pos=i;}i++;
        }
        return pos;
    }
}