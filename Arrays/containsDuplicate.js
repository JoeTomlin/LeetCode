//Given an integer array nums, 
// return true if any value appears at least twice in the array,
// and return false if every element is distinct. 

/**
 * @param {number[]} nums
 * @return {boolean}
 */

function containsDuplicate(nums) {
    const seen = new Set();
  
    for (let i = 0; i < nums.length; i++) {
      if (seen.has(nums[i])) {
        return true;
      }
      seen.add(nums[i]);
    }
  
    return false;
  }

//O(n)