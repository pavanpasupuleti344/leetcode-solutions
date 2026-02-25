class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()==0){return 0;}
        int r=0;
    List<Character> map=new ArrayList<>();
    for(int i=0;i<s.length();i++){
        // left=0;
        while(map.contains(s.charAt(i))){
            map.remove(0);
        }
        map.add(s.charAt(i));
        r=Math.max(r,map.size());
    }
    return r;
    }
}