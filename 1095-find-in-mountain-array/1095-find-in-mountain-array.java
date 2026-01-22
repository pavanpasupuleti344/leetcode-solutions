/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int n=mountainArr.length();
        int low=0;
        int end=n-1;
        while(low<end){
            int mid=low+(end-low)/2;
            if(mountainArr.get(mid)<mountainArr.get(mid+1)){
                low=mid+1;
            }
            else{
                end=mid;
            }
        }
        int a1=bi(mountainArr,target,0,end,true);
        int a2=bi(mountainArr,target,end+1,n-1,false);
        if(a1!=-1){return a1;}
        else return a2;
    }
    public int bi(MountainArray arr,int t,int lowi,int high,boolean asc){
        int low=lowi;
        int end=high;
        while(low<=end){
            int mid=low+(end-low)/2;
            if(t==arr.get(mid)){return mid;}
            if(asc){
            if(t>arr.get(mid)){
                low=mid+1;
            }
            else{
                end=mid-1;
            }}
            else{
            if(t<arr.get(mid)){
                low=mid+1;
            }
            else{
                end=mid-1;
            }}
        }
        return -1;
    }
    // public int bid(MountainArray arr,int t,int lowi,int high){
    //     int low=lowi;
    //     int end=high;
    //     while(low<=end){
    //         int mid=low+(end-low)/2;
    //         if(t==arr.get(mid)){return mid;}
    //         else if(t<arr.get(mid)){
    //             low=mid+1;
    //         }
    //         else{
    //             end=mid-1;
    //         }
    //     }
    //     return -1;
    // }
}