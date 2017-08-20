// Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

// Note: The solution set must not contain duplicate triplets.

// For example, given array S = [-1, 0, 1, 2, -1, -4],

// A solution set is:
// [
//   [-1, 0, 1],
//   [-1, -1, 2]
// ]
// exceeds memeory limit
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    var res = [];
    nums.sort(function(a, b) {
      return a - b;
    });
    nums.forEach((num, ind) => {
      if (ind === 0 || num != nums[ind - 1]) {
        let r = twoSum(nums.slice(ind + 1), num);
        if (r.length > 0) {
          r.map(arr => {
            res.push(arr)
          });
        }
      }
    })
    return res;
};

var twoSum = function(numbers, target) {
    var index1 = 0;
    var index2 = numbers.length - 1;
    var res = [];
    while (index1 < index2) {
      if (numbers[index1] + numbers[index2] < -target)
        index1++;
      else if (numbers[index1] + numbers[index2] > -target)
        index2--;
      else {
        res.push([numbers[index1], numbers[index2], target]);
        while (index1 < index2 && numbers[index1] == numbers[index1+1])
          index1++;
        while (index1 < index2 && numbers[index2] == numbers[index2-1])
          index2--;
        index1++;
        index2--;
      }
    }
    return res;
};

console.log(threeSum([0,0,0]));

function debugTask(identity) {
    if (!(this instanceof debugTask)) {
        var tmp = new debugTask();
        tmp.identity = identity;
        return tmp;
    }
}

debugTask.prototype.handleRequest = function(typedRequest, opts, handle) {
    console.log('debugger' + this.identity + ' handling request');
};
debugTask.prototype.handleResponse = function(err, value, handle) {
    console.log('debugger' + this.identity + ' handling response');
};

var a = debugTask('123')
console.log(a);

a.handleRequest(null, null, null)
