//
// Created by XiaowenZhang on 10/17/16.
//

// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int i = 1, j = n;
        while (j > i) {
            int g = i + (j - i) / 2;
            if (guess(g) < 0) {
                j = g - 1;
            }
            else if (guess(g) > 0) {
                i = g + 1;
            }
            else {
                return g;
            }
        }
        return i;
    }
};