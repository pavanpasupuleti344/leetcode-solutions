class Solution {
    public int centeredSubarrays(int[] nums) {
        int[] pi=new int[nums.length];
        pi[0]=nums[0];
        for(int i=1;i<nums.length;i++){
            pi[i]=pi[i-1]+nums[i];
        }
        int c=nums.length;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(search(i,j,nums,pi)){c++;}
            }
        }
        return c;
    }    
    private static boolean search(int i,int j,int[] nums,int[] pi){
        int sum=0;
        if(i==0){sum=pi[j];}
        else{sum=pi[j]-pi[i-1];}
        for(int k=i;k<=j;k++){
            if(nums[k]==sum) return true;
        }
        return false;
    }
}