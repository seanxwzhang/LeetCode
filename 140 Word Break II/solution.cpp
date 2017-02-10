// Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

// Return all such possible sentences.

// For example, given
// s = "catsanddog",
// dict = ["cat", "cats", "and", "sand", "dog"].

// A solution is ["cats and dog", "cat sand dog"].

// UPDATE (2017/1/4):
// The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

// TODO: finish it!

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<string> res;
        vector<vector<string>> ok(s.length() + 1, false); //ok[i] stores if there exists a segmentation for s.substr(0, i + 1);
        ok[0] = true;
        for (int i = 0; i < s.length(); i++) { // i is the starting index
            for (int j = 1; j <= s.length() - i; j++) { // j is the length
                if (ok[i]) {
                    if (wordSet.count(s.substr(i, j)) > 0) {
                        ok[i+j] = 1;
                        if (i+j == s.length()) 
                           res.
                    }   
                } else {
                    break;
                }
            }
        }
        return ok.back();
    }
};