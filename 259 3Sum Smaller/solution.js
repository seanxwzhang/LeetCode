// Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

// For example, given nums = [-2, 0, 1, 3], and target = 2.

// Return 2. Because there are two triplets which sums are less than 2:

// [-2, 0, 1]
// [-2, 0, 3]

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumSmaller = function(nums, target) {
    var counter = 0;
    nums.sort((a,b) => {return a-b;});
    for (let k = 0; k < nums.length; k++) {
        let i = 0;
        let j = k - 1;
        while(i < j) {
            if (nums[j] + nums[k] + nums[i] >= target)
                j--;
            else {
                counter += j - i;
                i++;
            }
        }
    }
    return counter;
};

console.log(threeSumSmaller([1,-2,2,1,0], 1));