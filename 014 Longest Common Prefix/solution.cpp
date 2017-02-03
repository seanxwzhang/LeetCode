// Write a function to find the longest common prefix string amongst an array of strings.

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty())
          return "";
        string _prefix;
        for (int i = 0; i < strs[0].length(); i++) {
          char tmp = strs[0][i];
          for (int j = 1; j < strs.size(); j++) {
            if (tmp != strs[j][i])
              return _prefix;
          }
          _prefix += strs[0][i];
        }
        return _prefix;
    }
};