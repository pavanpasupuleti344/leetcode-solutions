class Solution {
    public int[] searchRange(int[] nums, int target) {
        int start=findFirst(nums,target);
        int last=findLast(nums,target);
        return new int[]{start,last};
    }
    private int findFirst(int[] nums,int target){
        int low=0;
        int high=nums.length-1;
        int ans=-1;
        while(low<=high){
            int mid=low + (high-low)/2;
            if(target==nums[mid]){
                ans=mid;
                high=mid-1;
            }
            else if(target<nums[mid]){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return ans;
    }
    private int findLast(int[] nums,int target){
        int low=0;
        int high=nums.length-1;
        int ans=-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(target==nums[mid]){
                ans=mid;
                low=mid+1;
            }
            else if(target>nums[mid]){
                low=mid+1;
            }
            else{
                high=mid-1;
            }
        }
        return ans;
    }
}