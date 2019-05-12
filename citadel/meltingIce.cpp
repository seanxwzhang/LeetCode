#include <vector>
#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

// 这周突然收到的面试，不面白不面吧，虽然感觉应该拿不到。刚面完热乎的面经，45分钟，一道题：
// 给一个时间为0时刻的board，每个点有三种值：I代表ice，T代表treasure，.代表空地，时间每+1，上下左右四个方向里有一个方向不是ice的ice会融化成空地。treasure只有一个。定义如果treasure可以由某一个边出发访问到（只能走空地，不能走ice），称treasure是accessible的，问经过多少时间treasure可以变的accessible。
class Solution {
public:
  int meltingIce(const vector<string>& i_map) {
    // find treasure location
    // create an accessible map
    // create a queue for melting ice
    // populate the queue with BFS
    // every second
    //    1. melt ice, update accessible map accordingly
    //    2. if treasure accessible, return time
    //    3. add new melting ice to the melting queue
    //    4. switch queue
    


  }


};

int main() {
  vector<string> char_map {
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIII.IIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "III.IIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIISIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII",
  "IIIIIIIII.IIIIIIIIIIIIIIIIII",
  "IIIIIIIIIIIIIIIIIIIIIIIIIIII"};
  s = Solution();
  cout << s.meltingIce(char_map) << " seconds is required to access treasure.";
  return 0;
}
