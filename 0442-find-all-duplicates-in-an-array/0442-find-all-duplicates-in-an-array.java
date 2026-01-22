class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> m=new ArrayList<>();
        int i=0;
        while(i<nums.length){
            int c=nums[i]-1;
            if(nums[i]<=nums.length&&nums[i]!=nums[c]){
                swap(nums,i,c);
            }
            else i++;
        }
        for(int j=0;j<nums.length;j++){
            if(nums[j]!=j+1){m.add(nums[j]);}
        }
        return m;
    }
    static void swap(int[] a,int i,int j){
        int temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
}