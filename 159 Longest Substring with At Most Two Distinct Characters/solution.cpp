class Solution{
public:
	int longest_substring_two(string s) {
		int i = 0, j = 0, maxlen = 0;
		unordered_map<char, int> exists;
		for (; j < s.length(); j++) {
			while(exists.size() == 2 && exists.count[s.at(j)] == 0) {
				exists[s.at(i)]--;
				if (exists[s.at(i)] == 0) {
					exists.erase(s.at(i++));
				}
			}
			exists[s.at(j)]++;
			maxlen = (maxlen > (j - i) + 1) ? maxlen : j - i + 1;
		}
		return maxlen;
	}
};
