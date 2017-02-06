// Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

//     For example, given array S = {-1 2 1 -4}, and target = 1.

//     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    var _sum;
    nums.sort((a,b) => {return a-b;});
    for(let i = 0; i < nums.length; i++) {
        let j = i + 1;
        let k = nums.length - 1;
        while(j < k) {
            let _tmp = nums[i] + nums[j] + nums[k];
            if (_sum === undefined || Math.abs(_tmp - target) < Math.abs(_sum - target))
                _sum = _tmp;
            if (target - _tmp > 0)
                j++;
            else if (target - _tmp < 0)
                k--;
            else
                return target;
        }
    }
    return _sum;
};