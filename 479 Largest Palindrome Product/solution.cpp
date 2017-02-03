// # Find the largest palindrome made from the product of two n-digit numbers.
// #
// # Since the result could be very large, you should return the largest palindrome mod 1337.
// #
// # Example:
// #
// # Input: 2
// #
// # Output: 987
// #
// # Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
// #
// # Note:
// #
// # The range of n is [1,8].

// Approach: count down the palindrome, check if it is a product of two n-digit number
// since we know the for n >= 2, the palindrome will have 2n digits, the getPalindrome function is easy to write
#include <string>
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    long long getPalindrome(int m) {
      string left = to_string(m);
      string right = left;
      reverse(right.begin(), right.end());
      left+=right;
      return atoll(left.c_str());
    }

    bool isDecomposable(long long pal, int _max) {
      int _root = int(sqrt(pal));
      while(_root > 0 && (pal / _root) <= _max) {
        if (!(pal % _root--)) {
          return true;
        }
      }
      return false;
    }

    int largestPalindrome(int n) {
      if (n == 1)
        return 9;
      int _max = pow(10, n) - 1, _num = _max;
      while (_num > 0) {
        long long pal = getPalindrome(_num--);
        if (isDecomposable(pal, _max)) {
          return (pal % 1337);
        }
      }
      return 0;
    }
};

int main() {
  auto s = Solution();
  cout << s.largestPalindrome(8) << endl;
}