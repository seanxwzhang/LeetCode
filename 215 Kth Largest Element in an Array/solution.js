// Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

// For example,
// Given [3,2,1,5,6,4] and k = 2, return 5.

// Note: 
// You may assume k is always valid, 1 ≤ k ≤ array's length.

// Credits:
// Special thanks to @mithmatt for adding this problem and creating all test cases.


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */


var findKthLargest1 = function(nums, k) {
    nums.sort((a,b) => {return b-a;});
    return nums[k - 1];
};

Array.prototype.swap = function (x,y) {
  var b = this[x];
  this[x] = this[y];
  this[y] = b;
  return this;
}
/**
 * This approach use quicksort, but stop when the partition is at the kth largest element
 */
var findKthLargest2 = function(nums, k, l, r) {
    var partition = function(arr, left, right) {
        var x = arr[right];
        var i = left;
        for (let j = left; j < right; j++) {
            if (arr[j] <= x) 
                arr.swap(i++, j);
        }
        arr.swap(i, right);
        return i;
    };
    var p = partition(nums, l, r);
    // if partition 
    if (p == (nums.length - k))
        return nums[p];
    else if (p < (nums.length - k))
        return findKthLargest2(nums, k, p + 1, r);
    else
        return findKthLargest2(nums, k, l, p - 1);
}

var findKthLargest = function(nums, k) {
    return findKthLargest2(nums, k, 0, nums.length - 1);
}

console.log(findKthLargest([1,3,6,4,8,22,54,2,51,68,42,56],5));