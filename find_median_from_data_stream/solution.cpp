//
// Created by XiaowenZhang on 11/2/16.
//
#include <queue>
#include <iostream>

using namespace std;

class MedianFinder {

public:
    priority_queue<long> large, small;
    // Adds a number into the data structure.
    void addNum(int num) {
        small.push((long)num);
        large.push(-small.top());
        small.pop();
        if (large.size() > small.size() + 1) {
            small.push(-large.top());
            large.pop();
        }
    }

    // Returns the median of current data stream
    double findMedian() {
        if (large.size() > small.size()) {
            return (double)(-large.top());
        }
        else {
            return ((double)(-large.top()) + (double)small.top()) / 2;
        }
    }
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf;
// mf.addNum(1);
// mf.findMedian();

int main() {
    MedianFinder mf;
    mf.addNum(2);
    cout << mf.findMedian();
    mf.addNum(3);
    cout << mf.findMedian();
}