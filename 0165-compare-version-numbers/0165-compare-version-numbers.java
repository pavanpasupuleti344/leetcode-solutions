class Solution {
    public int compareVersion(String version1, String version2) {
        String[] n1=version1.split("\\.");
        String[] n2=version2.split("\\.");
        int n=Math.max(n1.length,n2.length);
        for(int i=0;i<n;i++){
            int num1=(i<n1.length)?Integer.parseInt(n1[i]):0;
            int num2=(i<n2.length)?Integer.parseInt(n2[i]):0;
            if(num1<num2) return -1;
            if(num1>num2) return 1;
        }
        return 0;
    }
}