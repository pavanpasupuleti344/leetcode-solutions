class Solution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long c=0;
        int min=Math.min(need1,need2);
        if(cost1+cost2>=costBoth){
             c+=(long)costBoth*min;
            need1-=min;
            need2-=min;
        }
        c+=(long)Math.min(cost1,costBoth)*need1;
        c+=(long)Math.min(cost2,costBoth)*need2;
        return c;
    }
}