'''
Created on Feb 26, 2016

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

@author: Cigarent
'''
class Solution(object):  
    def twoSum(self, nums, target):  
        """ 
        :type nums: List[int] 
        :type target: int 
        :rtype: List[int] 
        """  
        snums = set(nums)  
        for i, v in enumerate(nums):  
            if target - v in snums and target - v in nums[i+1:]:  
                return [i, nums[i+1:].index(target - v)+i+1]  