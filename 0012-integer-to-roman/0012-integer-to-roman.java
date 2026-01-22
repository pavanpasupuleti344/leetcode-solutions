class Solution {
    public String intToRoman(int num) {
        String n="";
        while(num>=1000){
            num-=1000;
            //System.out.print("M");
            n+="M";
        }
        while(num>=900){
            num-=900;
            //System.out.print("D");
            n+="CM";
        }
         while(num>=500){
            num-=500;
            //System.out.print("C");
            n+="D";
        }
         while(num>=400){
            num-=400;
            //System.out.print("L");
            n+="CD";
        }
         while(num>=100){
            num-=100;
           // System.out.print("X");
           n+="C";
        }
         while(num>=90){
            num-=90;
            //System.out.print("DV");
            n+="XC";
        }
         while(num>=50){
            num-=50;
           // System.out.print("I");
           n+="L";
        }
         while(num>=40){
            num-=40;
           // System.out.print("I");
           n+="XL";
        }
         while(num>=10){
            num-=10;
           // System.out.print("I");
           n+="X";
        }
         while(num>=9){
            num-=9;
           // System.out.print("I");
           n+="IX";
        }
         while(num>=5){
            num-=5;
           // System.out.print("I");
           n+="V";
        }
         while(num>=4){
            num-=4;
           // System.out.print("I");
           n+="IV";
        } while(num>=1){
            num-=1;
           // System.out.print("I");
           n+="I";
        }
        return n;
    }
}