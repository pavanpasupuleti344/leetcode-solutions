class Solution {
    public boolean makeEqual(String[] words) {
        HashMap<Character,Integer> m=new HashMap<>();
        for(String s:words){
            for(int i=0;i<s.length();i++){
                m.put(s.charAt(i),m.getOrDefault(s.charAt(i),0)+1);
            }
        }
        System.out.println(m);
        for(int i:m.values()){
            if(i%(words.length)!=0){
                return false;
            }
        }
        return true;
    }
}