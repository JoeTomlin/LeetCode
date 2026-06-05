# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

def twoSum(numbers, target):
    L, R = 0, len(numbers) - 1

    while L < R:
        current_sum = numbers[L] + numbers[R]
        if current_sum == target:
            return [L+1, R+1]
        elif current_sum < target:
            L += 1
        else:
            R -= 1
    return [-1, -1]

# O(n) time
# O(1) space