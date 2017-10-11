#include<vector>

using namespace std;

class Vector2D {
private:
    vector<vector<int>>::iterator row;
    vector<int>::iterator col;
    vector<vector<int>> nums;
public:
    Vector2D(vector<vector<int>> &nums): nums{nums} {
        row = nums.begin();
        if (row != nums.end()) col = row->begin();
    }

    int next() {
        if (hasNext()) return *(col++);
        throw "I'm empty";
    }

    bool hasNext() {
        while (row != nums.end() && col == row->end()) {
            ++row;
            if (row != nums.end()) col = row->begin();
        }
        return row != nums.end();
    }

    void remove() {
        if (col == row->begin()) {
            auto pre = prev(row);
            while (pre != nums.begin() && pre->empty()) {
                pre = prev(pre);
            }
            if (!pre->empty()) {
                pre->erase(prev(pre->end()));
            } else {
                throw "should call next() first!";
            }
        } else {
            col = row->erase(prev(col));
        }
    }
};

