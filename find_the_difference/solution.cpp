//
// Created by XiaowenZhang on 10/27/16.
//
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    char findTheDifference(string s, string t) {
        int counter_s[26] = {0}, counter_t[26] = {0};
        for (auto i : s) {
            counter_s[size_t(i - 'a')]++;
        }
        for (auto j : t){
            if (++counter_t[size_t(j - 'a')] > counter_s[size_t(j - 'a')]){
                return j;
            }
        }
        return 'a';
    }
};

int main() {
    Solution* a = new Solution;
    cout << a->findTheDifference("", "y");
    return 0;
}