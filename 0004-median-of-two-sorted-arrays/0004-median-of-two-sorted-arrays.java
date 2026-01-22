import java.util.Arrays;
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] merge=new int[nums1.length+nums2.length];
        int k=0;
        double res;
        for(int i=0;i<nums1.length;i++){
           
           merge[k]=nums1[i];
           k++;
        
        }
        for(int i=0;i<nums2.length;i++){
           
           merge[k]=nums2[i];
           k++;
        
        }
        int l=merge.length;
        Arrays.sort(merge);
        if(l%2==0){
            res=(double)merge[l/2]+merge[(l/2)-1];
            res=res/2;

        }
        else
        res=(double)merge[l/2];

        return (double)res;


    }
}