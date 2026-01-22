class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int mid=0;
        int low=0;
        int high=arr.length-1;
        while(low<high){
            mid=low+(high-low)/2;
            if(arr[mid]<arr[mid+1]){
                low=mid+1;
            }
            else {
                high=mid;
            }
        }
        return high;
    }
}