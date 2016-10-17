#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution1 {
public:
    int maxProfit(vector<int>& prices) { // dynamic programming solution
        if (prices.empty() || prices.size() == 1) {
            return 0;
        }
        if (prices.size() == 2) {
            return max(prices[1] - prices[0], 0);
        }
        vector<int> res = {0}; // res[n] is the maximum profit from prices[0] to prices[n]
        for (size_t i = 1; i < prices.size(); i++) {
            int maxnum = 0;
            for (int k = i - 1;  (k - 2) >= 0; k--) {
                maxnum = max(prices[i] - prices[k] + res[k-2], maxnum);
                maxnum = max(maxnum, res[k - 2]);
                maxnum = max(maxnum, res[k - 1]);
                maxnum = max(maxnum, res[k]);
            }
            maxnum = max(res[i - 1], maxnum);
            maxnum = max(prices[i] - prices[1], maxnum);
            res.push_back(max(prices[i] - prices[0], maxnum));
        }
        return max(max(res[prices.size() - 1], res[prices.size() - 2]), res[prices.size() - 3]);
    }
};

class Solution2 {
public:
    int maxProfit(vector<int>& prices) { // dynamic programming solution
        int buy(INT_MIN), prev_buy, sell = 0, prev_sell = 0;
        for (auto price : prices) {
            prev_buy = buy;
            buy = max(prev_sell - price, prev_buy);
            prev_sell = sell;
            sell = max(prev_buy + price, prev_sell);
        }
        return sell;
    }
};

int main() {
    vector<int> prices = {1,4,2};
    Solution1 *a = new Solution1;
    cout << a->maxProfit(prices);
    Solution2 *b = new Solution2;
    cout << b->maxProfit(prices);
}
