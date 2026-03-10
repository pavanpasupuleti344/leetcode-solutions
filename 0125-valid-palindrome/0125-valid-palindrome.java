class Solution {
    public boolean isPalindrome(String s) {
        int i=0;
        int end=s.length()-1;
        boolean ans=true;
        while(i<end){
            char start=s.charAt(i);
            char last=s.charAt(end);
            // int ch=s.charAt(i)-0;
            if(!Character.isLetterOrDigit(start)){
                i++;
                continue;
            }
            if(!Character.isLetterOrDigit(last)){
                end--;
                continue;
            }
            if(Character.toLowerCase(start)!=Character.toLowerCase(last)){
                ans=false;
                break;
            }
            i++;
            end--;
        }
        return ans;
    }
}