'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

class Solution(object):
    def searchInsert(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1


        while(l <= h):    
            m = (h + l) // 2

            if(target == nums[m]):
                return m
            elif(nums[m] > target):
                h = m - 1
            else:
                l = m + 1
        
        nums.insert(h+1, target)
        print(nums)
        return h + 1
        
nums = [1, 3, 5, 7]
target = 2
print('Res:', Solution().searchInsert(nums, target))