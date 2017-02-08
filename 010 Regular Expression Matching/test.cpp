
// Author :: Gaurav Ahirwar
#include <iostream>
#include <string>
using namespace std;

bool check_match(const char *s, const char *p) {

    if (!*p) return !(*s);
    if (p[1] == '*') return check_match(s, p+2) || (*p == '.' && *s || *s == *p) && check_match(s+1, p);
    if (*p == '.') return *s && check_match(s+1, p+1);
    return *s == *p && check_match(s+1, p+1);
}

int main() {
    string a("abc");
    cout << a[3] << endl;
    check_match("aa", "a") ? cout << "true\n" : cout << "false\n";
    check_match("aa", "aa") ? cout << "true\n" : cout << "false\n";
    check_match("aaa", "aa") ? cout << "true\n" : cout << "false\n";
    check_match("aa", "a*") ? cout << "true\n" : cout << "false\n";
    check_match("aa", ".*") ? cout << "true\n" : cout << "false\n";
    check_match("ab", ".*") ? cout << "true\n" : cout << "false\n";
    check_match("aab", "c*a*b") ? cout << "true\n" : cout << "false\n";
    check_match("aab", "c") ? cout << "true\n" : cout << "false\n";
    return 0;
}
