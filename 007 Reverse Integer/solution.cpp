// Reverse digits of an integer.
//
// Example1: x = 123, return 321
// Example2: x = -123, return -321

class Solution {
public:
    int reverse(int x) {
        if (!x) return x;
        int sign = x / abs(x);
        string sx = to_string(sign * x);
        std::reverse(sx.begin(), sx.end());
        return stoll(sx) > INT_MAX ? 0 : sign * atoi(sx.c_str());
    }
};
