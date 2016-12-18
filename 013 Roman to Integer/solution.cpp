//
// Created by sean on 12/18/16.
//
/*
 * Given a roman numeral, convert it to an integer.
 * Input is guaranteed to be within the range from 1 to 3999.
 */

#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int i = 0, l = s.length();
        unordered_map<char, int> map = {{'S', 0}, {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        int sum = 0;
        for (; i < l - 1; i++) {
            if (map[s[i]] < map[s[i+1]])
                sum -= map[s[i]];
            else
                sum += map[s[i]];
        }
        sum += map[s[l-1]];
        return sum;
    }
};

int main() {
    string s("CCVII");
    Solution ss;
    cout << ss.romanToInt(s) << endl;
    return 0;
}