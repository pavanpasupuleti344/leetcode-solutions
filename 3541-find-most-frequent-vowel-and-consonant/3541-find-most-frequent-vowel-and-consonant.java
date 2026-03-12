class Solution {
    public int maxFreqSum(String s) {
        String vowel="aeiou";
        HashMap<Character,Integer> map=new HashMap<>();
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            map.put(ch,map.getOrDefault(ch,0)+1);
        }
        int maxVo=0;
        int maxCo=0;
        for(char c:map.keySet()){
            if(vowel.indexOf(c)!=-1){
                maxVo=Math.max(maxVo,map.get(c));
            }
            else{
                maxCo=Math.max(maxCo,map.get(c));
            }
        }
        return maxCo+maxVo;
    }
}