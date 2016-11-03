#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int num_str = 0, num_query = 0;
    unordered_map<char*, int> strings;
    cin >> num_str;
    for (int i = 0; i < num_str; i++) {
        char tmp = new char[21];
        cin.geline(tmp, 21, '\n');
        strings[tmp] += 1;
    }
    cin >> num_query;
    for (int i = 0; i < num_query; i++) {
        char tmp[21];
        cin.getline(tmp, 21, '\n');
        cout << strings[tmp] << '\n';
    }
    return 0;
}
