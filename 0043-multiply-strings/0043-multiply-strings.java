class Solution {
    public String multiply(String num1, String num2) {
        long n1=Integer.parseInt(num1);
        long n2=Integer.parseInt(num2);
        if(n1*n2<=Integer.MIN_VALUE){return Integer.MIN_VALUE;}
        else if(n1*n2>=Integer.MAX_VALUE){return Integer.MAX_VALUE;}
        else return Integer.toString(n1*n2);
    }
}