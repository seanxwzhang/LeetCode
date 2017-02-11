// Given a collection of intervals, merge all overlapping intervals.

// For example,
// Given [1,3],[2,6],[8,10],[15,18],
// return [1,6],[8,10],[15,18].

/**
Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */

#include <vector>
#include <iostream>
using namespace std;
struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};

class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> res;
        sort(intervals.begin(), intervals.end(), [](const Interval & a, const Interval & b) { return a.start < b.start;});
        for (int i = 0; i < intervals.size(); i++) {
            if (i == 0)
                res.push_back(intervals[i]);
            else if (res.back().end >= intervals[i].start)
                res.back().end = max(res.back().end, intervals[i].end);
            else
                res.emplace_back(intervals[i].start, intervals[i].end);
        }
        return res;
    }
};

int main () {
    vector<Interval> a;
    a.emplace_back(1,4);
    a.emplace_back(2,5);
    auto s = Solution();
    auto res = s.merge(a);
    return 0;
}