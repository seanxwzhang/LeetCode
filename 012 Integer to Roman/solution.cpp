// Given an integer, convert it to a roman numeral.

// Input is guaranteed to be within the range from 1 to 3999.

// Symbol	I	V	X	L	C	D	M
// Value	1	5	10	50	100	500	1,000

// The numbers 1 to 10 are usually expressed in Roman numerals as follows:
// I, II, III, IV, V, VI, VII, VIII, IX, X.
// Numbers are formed by combining symbols and adding the values, so II is two (two ones) and XIII is thirteen (a ten and three ones). Because each numeral has a fixed value rather than representing multiples of ten, one hundred and so on, according to position, there is no need for "place keeping" zeros, as in numbers like 207 or 1066; those numbers are written as CCVII (two hundreds, a five and two ones) and MLXVI (a thousand, a fifty, a ten, a five and a one).
// Symbols are placed from left to right in order of value, starting with the largest. However, in a few specific cases,[2] to avoid four characters being repeated in succession (such as IIII or XXXX), subtractive notation is used: as in this table:[3][4]
// Number	4	9	40	90	400	900
// Notation	IV	IX	XL	XC	CD	CM

// Since the special cases are pretty hard to generalized, we hard-code the mapping

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        string _roman_chars[] = {"I", "IV" ,"V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM","M"};
        int _roman_values[] = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
        string res; int i = 12;
        while (i >= 0) {
          while (num / _roman_values[i]) {
            num -= _roman_values[i];
            res += _roman_chars[i];
          }
          i--;
        }
        return res;
    }
};

int main() {
  auto s = Solution();
  cout << s.intToRoman(2) << endl;
}