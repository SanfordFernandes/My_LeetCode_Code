'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''


def twoSum(nums, target):
    # Create a dictionary to store the complement of each number and its index
    complement_map = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement is in the dictionary
        if complement in complement_map:
            # Return the indices of the current number and its complement
            return [complement_map[complement], i]

        # Add the current number and its index to the dictionary
        complement_map[num] = i

    # If no solution is found, return an empty list
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]
