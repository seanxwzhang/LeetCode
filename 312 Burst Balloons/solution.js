// Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

// Find the maximum coins you can collect by bursting the balloons wisely.

// Note: 
// (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
// (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

// Example:

// Given [3, 1, 5, 8]

// Return 167

//     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
//    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


/**
 * @param {number[]} nums
 * @return {number}
 * The idea is to divide and conquer to decide where is the best burst point
 * Assuming all numbers are greater than 1
 * This solution is TLE, O(n!)
 */
var maxCoins1 = function(nums) {
    if (nums.length == 0)
        return 0;
    else if (nums.length == 1)
        return nums[0];
    else if (nums.length == 2)
        return nums[0] * nums[1] + Math.max(nums[0], nums[1]);
    else if ((nums.length) == 3) {
        return (nums[0] * nums[1] * nums[2] + nums[0] * nums[2] + Math.max(nums[0], nums[2]));
    } else {
        var _maxcoin = 0;
        for (let i = 0; i < nums.length; i++) {
            let bb = nums[i];
            if (i === 0)
                var burst = bb * nums[i+1];
            else if (i == nums.length - 1)
                var burst = bb * nums[i - 1];
            else
                var burst = bb * nums[i - 1] * nums[i + 1];
            nums.splice(i, 1);
            _maxcoin = Math.max(_maxcoin, burst + maxCoins(nums));
            nums.splice(i, 0, bb);
        }
        return _maxcoin;
    }
};

/**
 * This solution uses reverse linking, divide and conquer, and DP
 */
var maxCoins = function(nums) {
    nums.splice(0,0,1);
    nums.splice(nums.length, 0, 1);
    var n = nums.length;
    var dp = [];
    for (let i = 0; i < n; i++) {
        dp.push([]);
        for (let j = 0; j < n; j++) {
            dp[i].push(0);
        }
    }
    for (let k = 2; k < n; k++) {
        for (let left = 0; left < n - k; left++) {
            let right = left + k;
            for (let i = left + 1; i < right; i++) {
                dp[left][right] = Math.max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]);
            }
        }
    }
    return dp[0][n-1];
}

console.log(maxCoins([7,9,8,0,7,1,3,5,5,2,3]));