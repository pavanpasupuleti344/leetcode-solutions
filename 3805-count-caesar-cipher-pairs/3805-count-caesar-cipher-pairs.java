class Solution {
    public long countPairs(String[] words) {
        Map<String, Long> map = new HashMap<>();
        long ans = 0;
        for (String w : words) {
            String key = normalize(w);
            long cnt = map.getOrDefault(key, 0L);
            ans += cnt;
            map.put(key, cnt + 1);
        }
        return ans;
    }
    private String normalize(String s) {
        StringBuilder sb = new StringBuilder();
        int shift = s.charAt(0) - 'a';
        for (char c : s.toCharArray()) {
            char nc = (char) ((c - shift - 'a' + 26) % 26 + 'a');
            sb.append(nc);
        }
        return sb.toString();
    }
}