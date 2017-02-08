// '.' Matches any single character.
// '*' Matches zero or more of the preceding element.
//
// The matching should cover the entire input string (not partial).
//
// The function prototype should be:
// bool isMatch(const char *s, const char *p)
//
// Some examples:
// isMatch("aa","a") → false
// isMatch("aa","aa") → true
// isMatch("aaa","aa") → false
// isMatch("aa", "a*") → true
// isMatch("aa", ".*") → true
// isMatch("ab", ".*") → true
// isMatch("aab", "c*a*b") → true
// isMatch("ab", "a*b") -> true
// isMatch("abc", ".*") -> true
#include <string>
#include <iostream>
#include <utility>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.empty()) return s.empty();
        if (p.length() == 1) return (s.length() == 1) && (p[0] == s[0] || p[0] == '.');
        // if the next char is *, then do brutal force exhausting search of matching 0, 1, 2...
        if (p[1] == '*') return isMatch(s, p.substr(2)) || (!s.empty() && (p[0] == s[0] || p[0] == '.') && isMatch(s.substr(1), p));
        return !s.empty() && (p[0] == s[0] || p[0] == '.') && isMatch(s.substr(1), p.substr(1));
    }
};

int main() {
    Solution s;
    cout << s.isMatch("a", ".*..a*");
    return 0;
}
