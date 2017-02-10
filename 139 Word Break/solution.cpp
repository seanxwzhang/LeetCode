// Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

// For example, given
// s = "leetcode",
// dict = ["leet", "code"].

// Return true because "leetcode" can be segmented as "leet code".

// UPDATE (2017/1/4):
// The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<bool> ok(s.length() + 1, false); //ok[i] stores if there exists a segmentation for s.substr(0, i + 1);
        ok[0] = true;
        for (int i = 0; i < s.length(); i++) { // i is the starting index
            for (int j = 1; j <= s.length() - i; j++) { // j is the length
                if (ok[i]) {
                    ok[i+j] = ok[i+j] || wordSet.count(s.substr(i, j)) > 0;
                } else {
                    break;
                }
            }
        }
        return ok.back();
    }
};