class Solution {
    public int[] findOriginalArray(int[] changed) {
        int[] anse=new int[0];
        if(changed.length%2!=0){return anse;}
        int l=0;
        int[] ans=new int[changed.length/2];
        Arrays.sort(changed);
        int i=0;
        int k=i+1;
    while(i<changed.length-1&&k<changed.length){
        if(changed[i]==-1){;
            i++;
            k=i+1;}
        else if(changed[i]*2==changed[k]){
            ans[l]=changed[i];
            l++;
            changed[k]=-1;
            i++;
            k=i+1;
        }
        else{k++;}

    }
    if(l==changed.length/2){return ans;}
    else {return anse;}
    }
}