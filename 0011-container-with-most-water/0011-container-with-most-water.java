class Solution {
    public int maxArea(int[] height) {
        int max=0;
        int left=0;
        int right=height.length-1;
        int lev;int area;
        while(left<right){
            lev=Math.min(height[left],height[right]);
            area=lev*(right-left);
            max=Math.max(max,area);
            if(height[left]<height[right]){left++;}
            else right--;

        }
        return max;
    }
}