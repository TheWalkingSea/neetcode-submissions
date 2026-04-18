class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        HashMap<Character, Integer> scharmap = new HashMap<>();
        HashMap<Character, Integer> tcharmap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            scharmap.put(s.charAt(i), 1 + scharmap.getOrDefault(s.charAt(i), 0));
            tcharmap.put(t.charAt(i), 1 + tcharmap.getOrDefault(t.charAt(i), 0));
        }

        for (Map.Entry<Character, Integer> entry : scharmap.entrySet()) {
            Character key = entry.getKey();
            Integer value = entry.getValue();
            if (!tcharmap.getOrDefault(key, -1).equals(value)) {
                return false;
            }
        }
        return true;
    }
}
