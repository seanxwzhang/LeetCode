
#include <vector>
#include <iostream>
#include <unordered_map>
#include <string>
#include <queue>
#include <utility>

using namespace std;

// 这周突然收到的面试，不面白不面吧，虽然感觉应该拿不到。刚面完热乎的面经，45分钟，一道题：
// 给一个时间为0时刻的board，每个点有三种值：I代表ice，T代表treasure，.代表空地，时间每+1，上下左右四个方向里有一个方向不是ice的ice会融化成空地。treasure只有一个。定义如果treasure可以由某一个边出发访问到（只能走空地，不能走ice），称treasure是accessible的，问经过多少时间treasure可以变的accessible。
class Solution {
public:
  tuple<int, int> findTreasure(const vector<string>& i_map) {
    for (auto it = i_map.begin(); it != i_map.end(); it++) {
      for (auto cit = it->begin(); cit != it->end(); cit++) {
        if (*cit == 'S') {
          return make_tuple(it - i_map.begin(), cit - it->begin());
        }
      }
    }
  }


  int meltingIce(const vector<string>& i_map) {
    // find treasure location
    // create an accessible map
    // create a queue for melting ice
    // populate the queue with BFS
    // every second
    //    1. melt ice
    //    2. update accessible map accordingly
    //    3. if treasure accessible, return time
    //    4. add new melting ice to the melting queue
    //    5. switch queue
    auto loc = self.findTreasure(i_map);
    vector<vector<bool>> accessible(i_map.size(), vector<int>(i_map[0].size(), false));
    queue<pair<int, int>> melting_queue;
    



};

int main() {
  vector<string> char_map {
  "IIIIIIIIIIIIIII.IIIIIIIIIIII",
  "IIIIIIIIIIIIII...IIIIIIIIIII",
  "IIIIIIIIIIIIIII.IIIIIIIIIIII",
  "III.IIIIIIIIIII.IIIIIIIIIIII",
  "IIIIIIIIIIIIII...IIIIIIIIIII",
  "IIIIIIIIIIIII.....IIIIIIIIII",
  "IIIIIIIIIIIIII...IIIIIIIIIII",
  "IIIIIIIIIIIIIII.I.IIIIIIIIII",
  "IIIIIIIIIIIIIIII...IIIIIIIII",
  "IIIIIIIIIIIIIII..S..IIIIIIII",
  "IIIIIIIIIIIIIIII...IIIIIIIII",
  "IIIIIIIIIIIIIIIII.IIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIII.IIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII"};
  auto s = Solution();
  cout << s.meltingIce(char_map) << " seconds is required to access treasure.";
  cout << get<0>(s.findTreasure(char_map)) << "  " << get<1>(s.findTreasure(char_map));
  return 0;
}
