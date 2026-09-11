class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> m1;

        for (char c : s) m1[c]++;
        for (char c : t) if (--m1[c] < 0) return false;
    return true;
    }
};
