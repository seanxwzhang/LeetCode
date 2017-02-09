// Implement a basic calculator to evaluate a simple expression string.

// The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

// You may assume that the given expression is always valid.

// Some examples:
// "1 + 1" = 2
// " 2-1 + 2 " = 3
// "(1+(4+5+2)-3)+(6+8)" = 23
// Note: Do not use the eval built-in library function.

#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> st;
        int res = 0;
        int num = 0;
        int sign = 1;
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                num = 10 * num + (s[i] - '0');
            } else if (s[i] == '+') {
                res += sign * num;
                sign = 1;
                num = 0;
            } else if (s[i] == '-') {
                res += sign * num;
                sign = -1;
                num = 0;
            } else if (s[i] == '(') {
                st.push(res);
                st.push(sign);
                res = 0;
                sign = 1;
            } else if (s[i] == ')') {
                res += sign * num;
                int prevSign = st.top();
                st.pop();
                int prev = st.top();
                st.pop();
                res = prev + prevSign * res;
                sign = 1;
                num = 0;
            } 
        }
        if (num) { res += sign * num;}
        return res;
    }
};