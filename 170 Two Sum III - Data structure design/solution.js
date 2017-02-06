// Design and implement a TwoSum class. It should support the following operations: add and find.

// add - Add the number to an internal data structure.
// find - Find if there exists any pair of numbers which sum is equal to the value.

// For example,
// add(1); add(3); add(5);
// find(4) -> true
// find(7) -> false

/**
 * Initialize your data structure here.
 */
var TwoSum = function() {
    this.arr = [];

};

/**
 * Add the number to an internal data structure.. 
 * @param {number} number
 * @return {void}
 */
TwoSum.prototype.add = function(number) {
    var i = 0;
    var j = this.arr.length;
    while(i < j) {
      var mid = Math.floor((i + j) / 2);
      if (this.arr[mid] <= number) {
        i++;
      } else{
        j--;
      }
    }
    this.arr.splice((i+j)/2, 0, number);
};

/**
 * Find if there exists any pair of numbers which sum is equal to the value. 
 * @param {number} value
 * @return {boolean}
 */
TwoSum.prototype.find = function(value) {
    var index1 = 0;
    var index2 = this.arr.length - 1;
    while (index1 < index2) {
      if (this.arr[index1] + this.arr[index2] < value)
        index1++;
      else if (this.arr[index1] + this.arr[index2] > value)
        index2--;
      else
        return true;
    }
    return false;
};

/** 
 * Your TwoSum object will be instantiated and called as such:
 * var obj = Object.create(TwoSum).createNew()
 * obj.add(number)
 * var param_2 = obj.find(value)
 */

var a = new TwoSum();
a.add(3);
a.add(4);
a.add(5);
a.add(6);
a.add(7);
a.add(5);
a.add(2);