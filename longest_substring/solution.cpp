class Solution {
public:
    int lengthOfLongestSubstring(string s) {
  		// two pointer, O(n) time, O(1) space
		int i = 0, j = 0, length = 0;
		bool char_bucket[256] = {false};
		for (; j < s.length(); j++) {
			while(char_bucket[s.at(j)]) {
				char_bucket[s.at(i++)] = false;
			}
			length = (length > (j - i) + 1) ? length : j - i + 1;
			char_bucket[s.at(j)] = true;
		}
		return length;
    }
};
