//
// Created by XiaowenZhang on 11/2/16.
//
#include <vector>
#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        for (auto num : nums) {
            counter[num]++;
        }

        priority_queue<pair<int, int>> pq;
        vector<int> res;
        for (auto count : counter) {
            pq.push(make_pair(count.second, count.first));
        }
        for (int i = 0; i < k; i++) {
            res.push_back(pq.top().first);
            pq.pop();
        }
        return res;
    }
};