class Solution {
    public int firstMissingPositive(int[] nums) {
        int i=0;
        while(i<nums.length){
            if(nums[i]<=0){i++;continue;}
            int c=nums[i]-1;
            if(nums[i]<=nums.length&&nums[i]!=nums[c]){
                swap(nums,i,c);
            }
            else i++;
        }
        for(int j=0;j<nums.length;j++){
            if(nums[j]!=j+1){return j+1;}
        }
        return nums.length+1;
    }
    static void swap(int[] a,int i,int j){
        int temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
}