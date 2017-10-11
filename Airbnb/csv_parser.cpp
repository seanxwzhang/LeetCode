#include<vector>
#include<string>
#include<iostream>
using namespace std;

vector<string> parseCSV(string s) {
    vector<string> ans;
    bool inQuote = false;
    string tmp = "";
    for(int i = 0; i < s.length(); ++i) {
        if(inQuote) {
            if(s[i] == '"') {
                if(i == s.length() - 1) {
                    ans.push_back(tmp);
                    return ans;
                } else if(s[i + 1] == '"') {
                    tmp += '"';
                    ++i;
                } else {
                    ans.push_back(tmp);
                    tmp = "";
                    inQuote = false;
                    i++;
                }
            } else tmp += s[i];
        } else {
            if(s[i] == '"')
                inQuote = true;
            else if(s[i] == ',') {
                ans.push_back(tmp);
                tmp = "";
            } else tmp += s[i];
        }
    }
    if(!tmp.empty()) ans.push_back(tmp);
    return ans;
}

int main() {
    string ss[] = {"John,Smith,john.smith@gmail.com,Los Angeles,1", "\"Alexandra \"\"Alex\"\"\",Menendez,alex.menendez@gmail.com,Miami,1"};
    for(auto s : ss) {
        auto parsed = parseCSV(s);
        for (int i = 0; i < parsed.size() - 1; ++i)
            cout << parsed[i] << "|";
        cout<<parsed[parsed.size() - 1]<<endl;
    }
    return 0;
}
