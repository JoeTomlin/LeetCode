/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let n=0; n<nums.length-1; n++) {
        for (let increment = n + 1; increment < nums.length; increment++) {
            if (nums[n] + nums[increment] === target) {
                return [n, increment];
            }
        }
    }
};